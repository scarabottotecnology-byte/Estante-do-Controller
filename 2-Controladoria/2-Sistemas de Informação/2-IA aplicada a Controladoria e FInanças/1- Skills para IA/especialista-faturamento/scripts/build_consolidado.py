#!/usr/bin/env python3
"""Monta o workbook consolidado anual a partir dos pickles em cache/."""
import sys
import os
import glob
import pickle
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

MESES_PT = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
            7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

HEADER_FILL = PatternFill('solid', start_color='1F4E78')
HEADER_FONT = Font(bold=True, color='FFFFFF', name='Arial', size=10)
TITLE_FONT = Font(bold=True, size=14, name='Arial', color='1F4E78')
BOLD_FONT = Font(bold=True, name='Arial', size=10)
THIN = Side(border_style='thin', color='D0D0D0')
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
NUM_FMT = '#,##0.00'
PCT_FMT = '0.0%'


def style_header(ws, row, n_cols, start_col=1):
    for c in range(start_col, start_col + n_cols):
        cell = ws.cell(row, c)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal='center', vertical='center')
        cell.border = BORDER


def autosize(ws, max_width=40):
    for col_cells in ws.columns:
        length = max((len(str(c.value)) for c in col_cells if c.value is not None), default=8)
        col_letter = get_column_letter(col_cells[0].column)
        ws.column_dimensions[col_letter].width = min(max(length + 2, 10), max_width)


def main(cache_dir, output_path):
    pkls = sorted(glob.glob(os.path.join(cache_dir, '*.pkl')))
    if not pkls:
        print("Nenhum .pkl encontrado em", cache_dir)
        sys.exit(1)

    monthly_summary, bu_rows, canal_rows = [], [], []
    daily_frames, empresa_frames, cancel_rows, produtos_frames = [], [], [], []

    for p in pkls:
        with open(p, 'rb') as f:
            d = pickle.load(f)
        mes, ano, canal = d['mes'], d['ano'], d['canal']
        ped_sheet1 = d['empresa']['pedidos'].sum() if not d['empresa'].empty else 0
        # Dashboard "Nº Pedidos" de ambos os templates conta linhas da Sheet1, não pedidos únicos.
        # Usar sempre a contagem real de pedidos únicos extraída da Sheet1 (Nº Pedido).
        ped_final = ped_sheet1
        ticket_final = (d['total']['faturamento'] / ped_final) if ped_final else 0
        monthly_summary.append({
            'mes': mes, 'ano': ano, 'canal': canal,
            'faturamento': d['total']['faturamento'], 'pedidos': ped_final,
            'ticket_medio': ticket_final, 'itens': d['total']['itens'],
        })
        for nome_bu, vals in d['bu'].items():
            if nome_bu == 'TOTAL':
                continue
            bu_rows.append({'mes': mes, 'ano': ano, 'canal': canal, 'bu': nome_bu,
                             'faturamento': vals['faturamento'], 'pedidos': vals['pedidos'], 'itens': vals['itens']})
        for nome_canal, vals in d['canal_dash'].items():
            canal_rows.append({'mes': mes, 'ano': ano, 'canal_arquivo': canal, 'canal_venda': nome_canal,
                                'faturamento': vals['faturamento'], 'pedidos': vals['pedidos']})
        daily_frames.append(d['diario'])
        empresa_frames.append(d['empresa'])
        for _, row in d['cancelados'].iterrows():
            cancel_rows.append({'mes': mes, 'ano': ano, 'canal': canal,
                                 'bu': row['bu'], 'cancelado': row['cancelado'], 'qtd': row['qtd']})
        produtos_frames.append(d['produtos'])

    df_monthly = pd.DataFrame(monthly_summary)
    df_bu = pd.DataFrame(bu_rows)
    df_empresa = pd.concat(empresa_frames, ignore_index=True)
    df_daily = pd.concat(daily_frames, ignore_index=True)
    df_cancel = pd.DataFrame(cancel_rows)
    df_produtos = pd.concat(produtos_frames, ignore_index=True)

    wb = Workbook()

    # ---- Sheet 1: Visão Anual ----
    ws = wb.active
    ws.title = 'Visão Anual'
    ws['A1'] = 'VISÃO ANUAL DE FATURAMENTO — Grupo Oficial Farma'
    ws['A1'].font = TITLE_FONT

    for ano in sorted(df_monthly['ano'].unique()):
        row0 = ws.max_row + 2
        ws.cell(row0, 1, f'Ano {ano}').font = BOLD_FONT

        sub = df_monthly[df_monthly['ano'] == ano]
        pivot = sub.pivot_table(index='mes', columns='canal', values='faturamento', aggfunc='sum', fill_value=0)
        pivot['TOTAL'] = pivot.sum(axis=1)
        pivot_ped = sub.pivot_table(index='mes', columns='canal', values='pedidos', aggfunc='sum', fill_value=0)
        pivot_ped['TOTAL'] = pivot_ped.sum(axis=1)

        header_row = row0 + 1
        cols = ['Mês'] + [f'Fat. {c} (R$)' for c in pivot.columns] + \
               [f'Pedidos {c}' for c in pivot_ped.columns] + ['Ticket Médio (R$)']
        for j, h in enumerate(cols, 1):
            ws.cell(header_row, j, h)
        style_header(ws, header_row, len(cols))

        r = header_row + 1
        total_fat = {c: 0 for c in pivot.columns}
        total_ped = {c: 0 for c in pivot_ped.columns}
        for mes in sorted(pivot.index):
            ws.cell(r, 1, MESES_PT[mes])
            j = 2
            for c in pivot.columns:
                v = pivot.loc[mes, c]
                ws.cell(r, j, v).number_format = NUM_FMT
                total_fat[c] += v
                j += 1
            for c in pivot_ped.columns:
                v = int(pivot_ped.loc[mes, c])
                ws.cell(r, j, v)
                total_ped[c] += v
                j += 1
            fat_total = pivot.loc[mes, 'TOTAL']
            ped_total = pivot_ped.loc[mes, 'TOTAL']
            ws.cell(r, j, fat_total / ped_total if ped_total else 0).number_format = NUM_FMT
            r += 1

        ws.cell(r, 1, 'TOTAL ANO').font = BOLD_FONT
        j = 2
        for c in pivot.columns:
            ws.cell(r, j, total_fat[c]).font = BOLD_FONT
            ws.cell(r, j).number_format = NUM_FMT
            j += 1
        for c in pivot_ped.columns:
            ws.cell(r, j, total_ped[c]).font = BOLD_FONT
            j += 1
        ws.cell(r, j, total_fat['TOTAL'] / total_ped['TOTAL'] if total_ped['TOTAL'] else 0).font = BOLD_FONT
        ws.cell(r, j).number_format = NUM_FMT

    autosize(ws)

    # ---- Sheet 2: Por BU ----
    ws = wb.create_sheet('Por BU')
    ws['A1'] = 'FATURAMENTO POR UNIDADE DE NEGÓCIO (mensal)'
    ws['A1'].font = TITLE_FONT
    pivot_bu = df_bu.pivot_table(index=['ano', 'mes'], columns='bu', values='faturamento', aggfunc='sum', fill_value=0)
    header_row = 3
    cols = ['Ano', 'Mês'] + list(pivot_bu.columns) + ['TOTAL']
    for j, h in enumerate(cols, 1):
        ws.cell(header_row, j, h)
    style_header(ws, header_row, len(cols))
    r = header_row + 1
    for (ano, mes), row in pivot_bu.iterrows():
        ws.cell(r, 1, ano)
        ws.cell(r, 2, MESES_PT[mes])
        j = 3
        for v in row:
            ws.cell(r, j, v).number_format = NUM_FMT
            j += 1
        ws.cell(r, j, row.sum()).number_format = NUM_FMT
        ws.cell(r, j).font = BOLD_FONT
        r += 1
    autosize(ws)

    # ---- Sheet 3: Por Empresa / Loja / CNPJ ----
    ws = wb.create_sheet('Por Empresa-Loja')
    ws['A1'] = 'FATURAMENTO POR EMPRESA / LOJA / CNPJ (mensal)'
    ws['A1'].font = TITLE_FONT
    pivot_emp = df_empresa.pivot_table(index=['ano', 'mes', 'canal'], columns='empresa',
                                        values='faturamento', aggfunc='sum', fill_value=0)
    header_row = 3
    cols = ['Ano', 'Mês', 'Canal'] + list(pivot_emp.columns) + ['TOTAL']
    for j, h in enumerate(cols, 1):
        ws.cell(header_row, j, h)
    style_header(ws, header_row, len(cols))
    r = header_row + 1
    for (ano, mes, canal), row in pivot_emp.iterrows():
        ws.cell(r, 1, ano)
        ws.cell(r, 2, MESES_PT[mes])
        ws.cell(r, 3, canal)
        j = 4
        for v in row:
            ws.cell(r, j, v).number_format = NUM_FMT
            j += 1
        ws.cell(r, j, row.sum()).number_format = NUM_FMT
        ws.cell(r, j).font = BOLD_FONT
        r += 1
    autosize(ws, max_width=35)

    # ---- Pedidos por Empresa/Loja (segunda tabela na mesma aba) ----
    pivot_emp_ped = df_empresa.pivot_table(index=['ano', 'mes', 'canal'], columns='empresa',
                                            values='pedidos', aggfunc='sum', fill_value=0)
    row0 = ws.max_row + 3
    ws.cell(row0, 1, 'PEDIDOS POR EMPRESA / LOJA (mensal)').font = TITLE_FONT
    header_row = row0 + 1
    cols = ['Ano', 'Mês', 'Canal'] + list(pivot_emp_ped.columns)
    for j, h in enumerate(cols, 1):
        ws.cell(header_row, j, h)
    style_header(ws, header_row, len(cols))
    r = header_row + 1
    for (ano, mes, canal), row in pivot_emp_ped.iterrows():
        ws.cell(r, 1, ano)
        ws.cell(r, 2, MESES_PT[mes])
        ws.cell(r, 3, canal)
        j = 4
        for v in row:
            ws.cell(r, j, int(v))
            j += 1
        r += 1
    autosize(ws, max_width=35)

    # ---- Sheet 4: Sazonalidade Diária ----
    ws = wb.create_sheet('Sazonalidade Diária')
    ws['A1'] = 'FATURAMENTO DIÁRIO CONSOLIDADO (Onsite + Loja)'
    ws['A1'].font = TITLE_FONT

    df_daily_total = df_daily.groupby('data').agg(
        faturamento=('faturamento', 'sum'),
        qtde=('qtde', 'sum'),
        receb_30d=('receb_30d', 'sum'),
        receb_60d=('receb_60d', 'sum'),
        receb_90d=('receb_90d', 'sum'),
    ).reset_index().sort_values('data')
    dow_map = {0: 'segunda-feira', 1: 'terça-feira', 2: 'quarta-feira', 3: 'quinta-feira',
               4: 'sexta-feira', 5: 'sábado', 6: 'domingo'}
    df_daily_total['dia_semana'] = df_daily_total['data'].dt.weekday.map(dow_map)
    df_daily_total['ticket_medio'] = df_daily_total.apply(
        lambda x: x['faturamento'] / x['qtde'] if x['qtde'] else 0, axis=1)

    header_row = 3
    cols = ['Data', 'Dia da Semana', 'Faturamento (R$)', 'Qtde Vendida', 'Ticket Médio (R$)',
            'Receb. 30D', 'Receb. 60D', 'Receb. 90D']
    for j, h in enumerate(cols, 1):
        ws.cell(header_row, j, h)
    style_header(ws, header_row, len(cols))
    r = header_row + 1
    for _, row in df_daily_total.iterrows():
        ws.cell(r, 1, row['data'].strftime('%d/%m/%Y'))
        ws.cell(r, 2, row['dia_semana'])
        ws.cell(r, 3, row['faturamento']).number_format = NUM_FMT
        ws.cell(r, 4, int(row['qtde']))
        ws.cell(r, 5, row['ticket_medio']).number_format = NUM_FMT
        ws.cell(r, 6, row['receb_30d']).number_format = NUM_FMT
        ws.cell(r, 7, row['receb_60d']).number_format = NUM_FMT
        ws.cell(r, 8, row['receb_90d']).number_format = NUM_FMT
        r += 1
    autosize(ws)

    # ---- Sazonalidade por dia da semana ----
    ws2 = wb.create_sheet('Sazonalidade Dia Semana')
    ws2['A1'] = 'MÉDIA DE FATURAMENTO POR DIA DA SEMANA'
    ws2['A1'].font = TITLE_FONT
    order = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
    by_dow = df_daily_total.groupby('dia_semana').agg(
        faturamento_medio=('faturamento', 'mean'),
        qtde_media=('qtde', 'mean'),
        dias=('faturamento', 'count')
    ).reindex(order)
    header_row = 3
    cols = ['Dia da Semana', 'Faturamento Médio (R$)', 'Qtde Média', 'Nº Dias na Amostra']
    for j, h in enumerate(cols, 1):
        ws2.cell(header_row, j, h)
    style_header(ws2, header_row, len(cols))
    r = header_row + 1
    for dow, row in by_dow.iterrows():
        ws2.cell(r, 1, dow)
        ws2.cell(r, 2, row['faturamento_medio']).number_format = NUM_FMT
        ws2.cell(r, 3, row['qtde_media']).number_format = '#,##0'
        ws2.cell(r, 4, int(row['dias']))
        r += 1
    autosize(ws2)

    # ---- Sheet 5: Recebíveis ----
    ws = wb.create_sheet('Recebíveis')
    ws['A1'] = 'PROJEÇÃO DE RECEBÍVEIS (30/60/90 dias) — mensal'
    ws['A1'].font = TITLE_FONT
    ws['A3'] = ('Nota: "Receb. 30D/60D/90D" representam a projeção de recebimento futuro com base '
                 'nas regras de prazo por forma de pagamento. Para conciliação efetiva com extratos '
                 'da adquirente/banco e cálculo de inadimplência real, cruzar com os relatórios de '
                 'liquidação financeira (Yuno/Rede/banco) — ver aba "Cancelamentos" para proxy de perdas.')
    ws['A3'].font = Font(italic=True, size=9, color='808080')
    ws.merge_cells('A3:J3')

    df_daily['ano'] = df_daily['data'].dt.year
    df_daily['mes'] = df_daily['data'].dt.month
    pivot_receb_m = df_daily.groupby(['ano', 'mes', 'canal']).agg(
        faturamento=('faturamento', 'sum'),
        receb_30d=('receb_30d', 'sum'),
        receb_60d=('receb_60d', 'sum'),
        receb_90d=('receb_90d', 'sum'),
    ).reset_index()

    header_row = 5
    cols = ['Ano', 'Mês', 'Canal', 'Faturamento (R$)', 'Receb. 30D (R$)', '% s/ Fat.',
            'Receb. 60D (R$)', '% s/ Fat.', 'Receb. 90D (R$)', '% s/ Fat.']
    for j, h in enumerate(cols, 1):
        ws.cell(header_row, j, h)
    style_header(ws, header_row, len(cols))
    r = header_row + 1
    for _, row in pivot_receb_m.iterrows():
        fat = row['faturamento']
        ws.cell(r, 1, int(row['ano']))
        ws.cell(r, 2, MESES_PT[int(row['mes'])])
        ws.cell(r, 3, row['canal'])
        ws.cell(r, 4, fat).number_format = NUM_FMT
        ws.cell(r, 5, row['receb_30d']).number_format = NUM_FMT
        ws.cell(r, 6, (row['receb_30d'] / fat) if fat else 0).number_format = PCT_FMT
        ws.cell(r, 7, row['receb_60d']).number_format = NUM_FMT
        ws.cell(r, 8, (row['receb_60d'] / fat) if fat else 0).number_format = PCT_FMT
        ws.cell(r, 9, row['receb_90d']).number_format = NUM_FMT
        ws.cell(r, 10, (row['receb_90d'] / fat) if fat else 0).number_format = PCT_FMT
        r += 1
    autosize(ws)

    # ---- Sheet 6: Cancelamentos ----
    ws = wb.create_sheet('Cancelamentos')
    ws['A1'] = 'CANCELAMENTOS POR BU (mensal) — base Onsite'
    ws['A1'].font = TITLE_FONT
    if not df_cancel.empty:
        pivot_canc = df_cancel.pivot_table(index=['ano', 'mes'], columns='bu', values='cancelado',
                                            aggfunc='sum', fill_value=0)
        header_row = 3
        cols = ['Ano', 'Mês'] + list(pivot_canc.columns) + ['Total Cancelado (R$)']
        for j, h in enumerate(cols, 1):
            ws.cell(header_row, j, h)
        style_header(ws, header_row, len(cols))
        r = header_row + 1
        for (ano, mes), row in pivot_canc.iterrows():
            ws.cell(r, 1, ano)
            ws.cell(r, 2, MESES_PT[mes])
            j = 3
            for v in row:
                ws.cell(r, j, v).number_format = NUM_FMT
                j += 1
            ws.cell(r, j, row.sum()).number_format = NUM_FMT
            ws.cell(r, j).font = BOLD_FONT
            r += 1
    autosize(ws)

    # ---- Sheet 7: Top Produtos Ano ----
    ws = wb.create_sheet('Top Produtos Ano')
    ws['A1'] = 'CURVA ABC ANUAL — TOP PRODUTOS (consolidado todos os meses/canais)'
    ws['A1'].font = TITLE_FONT
    prod_agg = df_produtos.groupby(['sku', 'produto']).agg(
        faturamento=('faturamento', 'sum'),
        qtd=('qtd', 'sum'),
        cmv=('cmv', 'sum'),
    ).reset_index()
    prod_agg['mc'] = prod_agg['faturamento'] - prod_agg['cmv']
    prod_agg['mc_pct'] = prod_agg.apply(lambda x: x['mc'] / x['faturamento'] if x['faturamento'] else 0, axis=1)
    prod_agg = prod_agg.sort_values('faturamento', ascending=False).reset_index(drop=True)
    total_fat_prod = prod_agg['faturamento'].sum()
    prod_agg['acum_pct'] = (prod_agg['faturamento'].cumsum() / total_fat_prod)

    def curva(p):
        if p <= 0.8:
            return 'A'
        elif p <= 0.95:
            return 'B'
        return 'C'
    prod_agg['curva'] = prod_agg['acum_pct'].apply(curva)

    header_row = 3
    cols = ['Rank', 'SKU', 'Produto', 'Faturamento Ano (R$)', 'Qtd Ano', 'CMV (R$)', 'MC (R$)', 'MC %', 'Curva ABC']
    for j, h in enumerate(cols, 1):
        ws.cell(header_row, j, h)
    style_header(ws, header_row, len(cols))
    r = header_row + 1
    for i, row in prod_agg.head(150).iterrows():
        ws.cell(r, 1, i + 1)
        ws.cell(r, 2, row['sku'])
        ws.cell(r, 3, row['produto'])
        ws.cell(r, 4, row['faturamento']).number_format = NUM_FMT
        ws.cell(r, 5, row['qtd']).number_format = '#,##0'
        ws.cell(r, 6, row['cmv']).number_format = NUM_FMT
        ws.cell(r, 7, row['mc']).number_format = NUM_FMT
        ws.cell(r, 8, row['mc_pct']).number_format = PCT_FMT
        ws.cell(r, 9, row['curva'])
        r += 1
    autosize(ws, max_width=45)

    wb.save(output_path)
    print(f"Arquivo consolidado salvo em: {output_path}")
    print(f"Arquivos processados: {len(pkls)}")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

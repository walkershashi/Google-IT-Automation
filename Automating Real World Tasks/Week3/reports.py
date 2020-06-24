#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie


def generate(filename, title, additional_info, table_data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,20)

  # For optional part : Plotting a Pie Chart
  report_pie = Pie()
  report_pie.width = 550
  report_pie.height = 550
  report_pie.x = 0
  report_pie.y = -300

  make_cnt = {}

  report_pie.data = []
  report_pie.labels = []
  for each in table_data[1:]:
    if each[1].split(" ")[0] not in make_cnt:
      make_cnt[each[1].split(" ")[0]] = each[-1]
    else:
      make_cnt[each[1].split(" ")[0]] += each[-1]
  
  for make, cnt in make_cnt.items():
    report_pie.labels.append(make)
    report_pie.data.append(cnt)
  
  report_chart = Drawing()
  report_chart.add(report_pie)

  report.build([report_title, empty_line, report_info, empty_line, report_table, report_chart])

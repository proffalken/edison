# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
try:
	from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField,BAND_WIDTH, Label,ReportGroup
	from reportlab.lib.pagesizes import A5
	from reportlab.lib.units import cm
	from reportlab.lib.enums import TA_RIGHT, TA_CENTER

	class ReportCfgItem(Report):
		title = 'Server Audit'
		author = 'Matthew Macdonald-Wallace'

		page_size = landscape(A5)
		margin_left = 2*cm
		margin_top = 0.5*cm
		margin_right = 0.5*cm
		margin_bottom = 0.5*cm

		class band_detail(ReportBand):
			height = 0.5*cm
			elements=(
			    ObjectValue(attribute_name='Hostname', left=0.5*cm),
			    ObjectValue(attribute_name='Rack', left=3*cm),
			)
			
		class band_page_header(ReportBand):
		    height = 1.3*cm
		    elements = [
			    SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
				style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
			    Label(text="Hostname", top=0.8*cm, left=0.5*cm),
			    Label(text=u"Rack", top=0.8*cm, left=3*cm),
			    SystemField(expression=u'Page %(page_number)d of %(page_count)d', top=0.1*cm,
				width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
			    ]
		    borders = {'bottom': True}

		class band_page_footer(ReportBand):
		    height = 0.5*cm
		    elements = [
			    Label(text='Geraldo Reports', top=0.1*cm),
			    SystemField(expression=u'Printed in %(now:%Y, %b %d)s at %(now:%H:%M)s', top=0.1*cm,
				width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
			    ]
		    borders = {'top': True}

		groups = [
			ReportGroup(attribute_name = 'Hostname',
			    band_header = ReportBand(
				height = 0.7*cm,
				elements = [
				    ObjectValue(attribute_name='Hostname', left=0, top=0.1*cm, width=20*cm,
					get_value=lambda instance: 'Hostname: ' + (instance.Hostname),
					style={'fontName': 'Helvetica-Bold', 'fontSize': 12})
				    ],
				borders = {'bottom': True},
				)
			    ),
			]
except ImportError:
	geraldo_loaded = False


from bokeh.plotting import ColumnDataSource, figure, output_file, show
from bokeh.transform import linear_cmap,factor_cmap
from bokeh.palettes import Viridis256,Category10

def create_html(filepath,scatterdata):
    output_file(filepath)
    
    source = ColumnDataSource(scatterdata)
    
    TOOLTIPS = """
        <div>
            <div>
                <img
                    src="@imgs" height="200" alt="@imgs" width="200"
                    style="float: left; margin: 0px 15px 15px 0px;"
                    border="2"
                ></img>
            </div>
        </div>
    """
    
    p = figure(width=1000, height=1000, tooltips=TOOLTIPS,
               title="Mouse over the dots")
    # Define a color map based on the 'Viridis256' color palette
    #mapper = linear_cmap(field_name='label', palette=Viridis256, low=0, high=max(source.data['label']))
    mapper = factor_cmap(field_name='label', palette=Category10[10], factors=list(set(source.data['label'])))
    
    p.circle('x', 'y', size=20, source=source, fill_color=mapper, fill_alpha=0.5)
    
    show(p)
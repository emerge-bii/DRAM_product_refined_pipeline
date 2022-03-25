import altair as alt
import pandas as pd


product_refied = pd.read_csv('results/emerge_distilled_filtered/EMERGE_170222_product_refined.tsv', sep='\t', index_col=0)
product_refied.shape
product_refied_sum = pd.DataFrame(product_refied.apply(sum, axis=1), columns=['sum']).reset_index()
product_refied_sum.rename(columns={"index":"reaction"}, inplace=True)
source = product_refied_sum

bars = alt.Chart(source).mark_bar().encode(
    x='sum',
    y="reaction"
).properties(
    width=700,
    height=900
)


text = bars.mark_text(
    align='left',
    baseline='middle',
    dx=40  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='sum'
)

alt.renderers.enable('altair_viewer')
bars.save('product_refined_prevalance_bars.jpg')
bars.show()

alt.renderers.enable('mimetype')
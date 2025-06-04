import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

# Force plotly to open plots in your default web browser
pio.renderers.default = 'browser'

# Custom cumulative trapezoidal integration
def cumulative_trapezoid(y, x):
    dx = np.diff(x)
    avg_y = (y[:-1] + y[1:]) / 2
    integral = np.zeros_like(y)
    integral[1:] = np.cumsum(avg_y * dx)
    return integral

# Time range
t = np.linspace(0, 30, 300)

# Constants
epsilon1 = 100
lam1 = 0.1
mu1 = 0.03
init_pop_cont = 1000
Ave_cont = 500

epsilon2 = 50
lam2 = 0.08
mu2 = 0.04
init_pen_pop = 300
Ave_pen = 1000

init_lump_pop1 = 200
init_lump_pop2 = 150
Ave_lump1 = 2000
Ave_lump2 = 1800

# Contributors
term1 = (epsilon1 / (lam1 - mu1)) * np.exp((lam1 - mu1) * t)
term2 = init_pop_cont * np.exp((lam1 - mu1) * t)
entire_pop_cont = cumulative_trapezoid(term1 + term2, t)
total_cont = entire_pop_cont * Ave_cont

# Lump sum recipients
lump_pop1 = init_lump_pop1 * (1 - np.exp(-mu2 * t))
lump_pop2 = init_lump_pop2 * (1 - np.exp(-epsilon2 * t))
total_lump = lump_pop1 * Ave_lump1 + lump_pop2 * Ave_lump2

# Pension recipients
term3 = (epsilon2 / (lam2 - mu2)) * np.exp((lam2 - mu2) * t)
term4 = init_pen_pop * np.exp((lam2 - mu2) * t)
pen_pop = cumulative_trapezoid(term3 + term4, t)
total_pen = pen_pop * Ave_pen

# Plotly plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=total_cont, mode='lines', name='Total Contributions'))
fig.add_trace(go.Scatter(x=t, y=total_lump, mode='lines', name='Total Lump Sum Payments'))
fig.add_trace(go.Scatter(x=t, y=total_pen, mode='lines', name='Total Pension Payments'))

fig.update_layout(
    title='Pension System Cash Flows Over Time',
    xaxis_title='Time (years)',
    yaxis_title='Amount',
    template='plotly_white',
    legend_title='Flow Type',
    width=900,
    height=500
)

fig.show()
from nice_gui import ui
import matplotlib.pyplot as plt
from datetime import datetime

ui.label('Hello, Nice GUI!')

with ui.row() as row:
    with row.column() as left:
        left.label('Add an element:')
        left.button('Button 1', on_click=lambda: left.label('Nice!'))
    with row.column() as right:
        right.label("Update itself:")
        right.button('Button 2', on_click=lambda e: setattr(e.sender, 'text', e.sender.text + ' :)'))

with ui.row() as row:
    row.checkbox('Let''s check...', on_change=lambda e: row.label('Check!' if e.checked else 'Uncheck.'))

with ui.plot():
    plt.title('Some plot')
    plt.plot(range(10), [x**2 for x in range(10)])

time = ui.label('Time:')
def update_time():
    time.text = f'Time: {datetime.now().strftime("%H:%M:%S")}'
ui.timer(1.0, update_time)

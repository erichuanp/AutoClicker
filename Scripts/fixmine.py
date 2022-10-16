import Core as op

op.press('divide')
op.write('fix all')
op.press('Enter')

for i in range(3):
    op.click(1)
    op.click(0, 6)
    for j in range(20):
        op.click(0, 3)
        op.delay(1.2)

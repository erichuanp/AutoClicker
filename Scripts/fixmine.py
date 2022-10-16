import Core as op
times = 0
op.delay(5)
while True:
    op.delay(1)
    op.press('divide')
    op.write('fix all')
    op.press('Enter')

    for i in range(3):
        op.click(1)
        op.click(0, 6)
        for j in range(20):
            op.click(0, 3)
            op.delay(1.2)
    times += 1
    print('运行了' + str(times) + '次。')

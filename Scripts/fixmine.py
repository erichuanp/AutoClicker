import Core as op
times = 0
while True:
    op.delay(5)
    op.press('divide')
    op.write('fix all')
    op.press('Enter')

    for i in range(3):
        op.click(1)
        op.click(0, 24)
        for j in range(20):
            op.click(0, 12)
            op.delay(1.2)
    times += 1
    print('运行了' + str(times) + '次。')

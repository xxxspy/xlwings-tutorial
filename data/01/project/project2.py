import xlwings as xw
def hello():
    wb = xw.Workbook.caller()
    xw.Range('a1').value='hello'


@xw.func
def double_sum(x, y):
    """Returns twice the sum of the two arguments"""
    return 2*(x+y)


print double_sum(1,2)

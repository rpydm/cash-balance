class CashBalance():
  def manage(spend, change):
    # お手持ちの現金の各枚数を入力してください。
    cash = {
        "10000" : 4, "5000" : 1, "1000" : 4
      , "500" : 12, "100" : 34, "50" : 24
      , "10" : 23, "5" : 20, "1" : 36
    }
    cash_balance = 0
    for x in cash:
      cash[x] = cash[x] - spend[x]
      cash[x] = cash[x] + change[x]
      print(x + '円: ' + str(cash[x]) + '枚')
      cash_balance = cash_balance + int(x) * cash[x]
    print('現金残高: ' + str(cash_balance) + '円')

  def calc_num_of_each_cash(amount):
    bill10000 = amount // 10000
    bill5000 = amount % 10000 // 5000
    bill1000 = amount % 5000 // 1000
    coin = amount % 1000
    coin500 = coin // 500
    coin100 = coin % 500 // 100
    coin50 = coin % 100 // 50
    coin10 = coin % 50 // 10
    coin5 = coin % 10 // 5
    coin1 = coin % 5 // 1
    cash = {
       "10000" : bill10000, "5000" : bill5000, "1000" : bill1000
      , "500" : coin500, "100" : coin100, "50" : coin50
      , "10" : coin10, "5" : coin5, "1" : coin1
    }
    return cash

  def expense(price, pay_amount):
    change = pay_amount - price
    return change

  # ものサービスの金額を指定してください。
  price = 0
  spend = calc_num_of_each_cash(price)
  # お釣りを貰う前の支払額を指定してください。
  pay_amount = 0
  change = calc_num_of_each_cash(expense(price, pay_amount))
  manage(spend, change)

CashBalance()
# 実行後、manege()の配列cashの値を標準出力を見て変更してください。
# ATMなどで現金を引き出した場合も直接そこの値を変更してください。
class CashBalance():
  def manage(payed, change):
    # お手持ちの現金の各枚数を入力してください。
    cash = {
        "10000" : 4, "5000" : 1, "1000" : 4
      , "500" : 12, "100" : 34, "50" : 24
      , "10" : 23, "5" : 20, "1" : 36
    }
    cash_balance = 0
    for x in cash:
      cash[x] = cash[x] - payed[x]
      cash[x] = cash[x] + change[x]
      print(x + '円: ' + str(cash[x]) + '枚')
      cash_balance = cash_balance + int(x) * cash[x]
    print('現金残高: ' + str(cash_balance) + '円')

  def calculate(spend):
    bill10000 = spend // 10000
    bill5000 = spend % 10000 // 5000
    bill1000 = spend % 5000 // 1000
    coin = spend % 1000
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

  def expense(price, payed):
    change = payed - price
    return change

  # ものサービスの金額を入力してください。
  payed = calculate(0)
  # お釣りを求めます。expenseにものサービスの金額, 支払った金額を入力してください。
  change = calculate(expense(0, 0))
  manage(payed, change)

CashBalance()
# 実行しても manege().cash{} の値は変更されません。
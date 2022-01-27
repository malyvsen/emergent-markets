from tradezoo.market import Market, Account, BuyOrder, SellOrder


def test_exact_match():
    market = Market(
        accounts=[
            Account(cash_balance=1, stock_balance=1),
            Account(cash_balance=2, stock_balance=2),
        ],
        orders=[],
    )
    market.submit_(BuyOrder(market.accounts[0], price=0.5, volume=1))
    market.submit_(SellOrder(market.accounts[1], price=0.5, volume=1))
    assert market.orders == []
    assert market.accounts[0] == Account(cash_balance=0.5, stock_balance=2)
    assert market.accounts[1] == Account(cash_balance=2.5, stock_balance=1)


def test_price_mismatch():
    market = Market(
        accounts=[
            Account(cash_balance=5, stock_balance=5),
            Account(cash_balance=6, stock_balance=6),
        ],
        orders=[],
    )
    market.submit_(BuyOrder(market.accounts[0], price=2, volume=1))
    market.submit_(SellOrder(market.accounts[1], price=3, volume=1))
    assert len(market.orders) == 2
    assert market.accounts[0] == Account(cash_balance=5, stock_balance=5)
    assert market.accounts[1] == Account(cash_balance=6, stock_balance=6)


def test_crossed_price():
    market = Market(
        accounts=[
            Account(cash_balance=5, stock_balance=5),
            Account(cash_balance=6, stock_balance=6),
        ],
        orders=[],
    )
    market.submit_(BuyOrder(market.accounts[0], price=3, volume=1))
    market.submit_(SellOrder(market.accounts[1], price=2, volume=1))
    assert market.orders == []
    assert market.accounts[0] == Account(cash_balance=3, stock_balance=6)
    assert market.accounts[1] == Account(cash_balance=8, stock_balance=5)

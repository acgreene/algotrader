from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed

# Strategy: "Steve Burns 200 Day Crush" 
#   Buy S&P500 index ETF when it closes above the 200 day SMA at 
#   the last trading day of a month, sell when it closes below the
#   200 day SMA at the last trading day of a month. 

class BuyAndHoldStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        super(BuyAndHoldStrategy, self).__init__(feed)
        self.instrument = instrument
        self.setUseAdjustedValues(True) #accounts for dividends and split
        self.position = None #own 0 stock at start
        
    def onEnterOk(self, position):
        self.info(f"{position.getEntryOrder().getExecutionInfo()}")
        
    def onBars(self, bars):
        bar = bars[self.instrument]
        #self.info(bar.getClose()) 
        
        if self.position is None:
            close = bar.getAdjClose()
            broker = self.getBroker()
            cash = broker.getCash()
            
            quantity = cash / close
            self.position = self.enterLong(self.instrument, quantity)

feed = yahoofeed.Feed()
feed.addBarsFromCSV("spy", "backtest/burns_200_day_crush/data/spy.csv")

strategy = BuyAndHoldStrategy(feed, "spy")
strategy.run()
portfolio_value = strategy.getBroker().getEquity() + strategy.getBroker().getCash()
print(portfolio_value)

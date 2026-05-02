import yfinance as yf
from langchain.tools import tool
from Rag import create_rag_chain

@tool
def get_stock_data(ticker: str) -> str:
    """
    Get real-time stock data for any Indian or global stock.
    Input should be ticker symbol like RELIANCE.NS, TCS.NS, AAPL
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        hist = stock.history(period="1mo")

        current_price = info.get('currentPrice', 'N/A')
        prev_close = info.get('previousClose', 'N/A')

        # calculate change %
        if current_price != 'N/A' and prev_close != 'N/A':
            change_pct = ((current_price - prev_close) / prev_close) * 100
            change_str = f"{change_pct:.2f}%"
        else:
            change_str = 'N/A'

        # 1 month return
        if len(hist) > 0:
            monthly_return = ((hist['Close'][-1] / hist['Close'][0]) - 1) * 100
            monthly_str = f"{monthly_return:.2f}%"
        else:
            monthly_str = 'N/A'

        return f"""
            Stock: {ticker.upper()},
            Current Price:   ₹{current_price},
            Previous Close:  ₹{prev_close},
            Day Change:      {change_str},
            PE Ratio:        {info.get('trailingPE', 'N/A')},
            Market Cap:      ₹{info.get('marketCap', 'N/A')},
            52-Week High:    ₹{info.get('fiftyTwoWeekHigh', 'N/A')},
            52-Week Low:     ₹{info.get('fiftyTwoWeekLow', 'N/A')},
            1-Month Return:  {monthly_str},
            Sector:          {info.get('sector', 'N/A')}
            """
    except Exception as e:
        return f"Could not fetch data for {ticker}. Error: {str(e)}"
    
rag_chain=create_rag_chain()

@tool
def search_knowalge(query):
    """ Search  Zerodha Varsity knowledge base for financial concept
        PE ratio,fundamental analysis and stock market basic """
    
    response=rag_chain.invoke({"input":query})
    return response['answer']


# Correlation-in-Stock-Market

![Stocks](https://www.ruleoneinvesting.com/wp-content/uploads/2014/11/stock-market-trends-what-causes-stock-prices-to-change.jpg "Stocks ↑")


![GitHub top language](https://img.shields.io/github/languages/top/Sumanmhalsank02/Correlation-in-Stock-Market?color=orange&style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/Sumanmhalsank02/Correlation-in-Stock-Market?style=plastic)
![GitHub](https://img.shields.io/github/license/Sumanmhalsank02/Correlation-in-Stock-Market?style=plastic)


## Description
---

This repository is build to analyse how the behaviour of the Stocks are correlated. The `Correlation` is perfomed on the percentage change of the stock price instead of the stock price. 

To know more about Correlation in Stock Maret, I would recommend the following link [Correlation](https://www.investopedia.com/terms/c/correlation.asp "Investopedia.com"). Do check it out for a brief understanding!!
It's extremely useful if you want to create a Diversified portfolio


## Installation
---

1. Clone the repository
2. Ensure all the dependencies are installed


## Usage
---

1. Download the `SOURCE_Datasets` to the project directory
2. Copy the paths of all the csv datasets into the `Correlation1.py` file
3. Run the `Correlation.py` file 
4. Understand, Observe and Analyse how the Stock Prices are correlated


![Correlation](https://drive.google.com/uc?export=view&id=1lQTFD56V8elYneUavPp6LGgdT2xMIWuG "Correlation")

This is how the output will look like!!


Pandas has provided us with a `.corr()` function:
    ``` python
    correlation = Data_CP_Perc_Change.corr()
    ```
To know more about `.corr()`, Visit [pandas.DataFrame.corr](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html)


- Try the code with different Stock Prices datasets to get a deeper understanding of Correlation
- Have Fun!! 


## Dependencies
---

- pandas
- matplotlib.pyplot
- seaborn


## License
---

This repository is licensed under [Mit License](https://github.com/Sumanmhalsank02/Correlation-in-Stock-Market/blob/main/LICENSE)








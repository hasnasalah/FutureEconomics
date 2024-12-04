# FutureEconomics
<h1>Macroeconomic Forecasting Project: GDP Growth and Unemployment Rate Predictions</h1>

<p style="font-size:14px">
In this project I aim to forecast and the predict the United States Gross Domestic Product (GDP) growth and unemployment rate based on historical macroeconomic data.
From GDP, Unemployment rates, Governement expenditure and import & export.
</p>
<h2>Goals</h2>
<ol>
   <li>Predict GDP Growth: Using historical data and macroeconomic factors, forecast future GDP growth in the U.S.</li>
   <li>Forecast Unemployment Rate: Predict fluctuations in the unemployment rate based on variables like inflation, industrial production, and other economic indicators.</li>

<h2>Dataset Sources</h2>
<ul>
<li>The dataset contains historical data on GDP, unemployment rate, inflation, interest rates, and government spending for the U.S. from reliable sources such as the <strong>Federal Reserve Economic Data (FRED)</strong> and<strong> the Bureau of Economic Analysis (BEA).</strong></li>
<li>The data has been sourced from both public APIs and offline data files.</li>
</ul>

<h2>Data Analysis and Visualization</h2>
In this project, we analyze key economic indicators, including GDP, unemployment rate, inflation, and government spending, to gain insights into economic trends. We visualize these indicators over time and apply statistical methods to better understand long-term trends and fluctuations.
<h3>OLS Regression Analysis:</h3>
Ordinary Least Squares (OLS) regression is used to model the relationship between economic indicators like GDP and various independent variables, such as unemployment rate, government spending, and interest rates. By performing OLS regression, we can estimate how much each of these factors influences GDP growth.
<h3>We used OLS regression to obtain:</h3>

<ol>
<li><strong>Coefficients:</strong> These represent the impact of each independent variable on GDP. For example, a positive coefficient means that as the independent variable increases, GDP is also expected to increase.</li>
<li><strong>R-squared value:</strong> This measures how well the model fits the data. An R-squared value close to 1 means the model explains most of the variance in GDP.</li>
<li><strong>P-values:</strong> These indicate the significance of each variable. A lower p-value (typically below 0.05) suggests that the corresponding predictor is statistically significant.</li>

<h3>Rolling Mean/Moving Average</h3>
A rolling mean (also known as a moving average) is applied to the GDP and unemployment time series data to smooth out short-term fluctuations. This method helps eliminate noise and highlights underlying trends over time. By calculating the average of values over a specified window (e.g., 5 years), we can better visualize the long-term trajectory of these economic indicators.

This technique is verry good for:
<ul>
<li>Identifying consistent long-term trends in GDP and unemployment.</li>
<li>Improving the clarity of time-series data by reducing random noise.</li>
<li>Making it easier to forecast future values of economic indicators.</li>
<h3>Correlation Matrix:</h3>
The correlation matrix is used to assess the linear relationships between pairs of economic indicators. Correlation values range from -1 to 1, where:
<ul>
<li>1 means a perfect positive correlation (both variables move in the same direction)</li>
<li>-1 means a perfect negative correlation (both variables move in opposite directions)</li>
</li>0 means no correlation (no predictable relationship).</li>
<strong>Why Use Correlation in this Project?</strong>
We use the correlation matrix to identify how closely  the key economic variables are related to each other. For example, if GDP and government spending are strongly correlated, it suggests that changes in government spending are likely to have a significant impact on GDP. The correlation matrix helps us prioritize which variables are most important to include in predictive models like OLS regression.

<h2>Tools and Technologies</h2>
<ul>
    <li>Programming Language: Python</li>
    <li>Data Analysis Libraries: pandas, numpy</li>
    <li>Visualization: matplotlib, seaborn</li>
    <li>APIs: FRED API, BEA API (to pull real-time data)</li>
    <li>Database: MySQL (for data storage and management)</li>
    <li>IDE: VS Code for code development and experimentation</li>
<h2>Setup Instructions</h2>
<h3>Requirements:</h3>
<ul>
<li>Python 3.6+
<li>Libraries: The following Python libraries are required:
<ul>
<li>pandas</li>
<li>numpy</li>
<li>statsmodels</li>
<li>matplotlib</li></ul></ul>
<h2>Installation Steps:</h2>
Clone or download this repository to your local machine using the following url:

Open Visual Studio Code and open the project folder.

Set up the Virtual Environment:

Open the terminal in Visual Studio Code (View > Terminal).
Navigate to your project directory if not already there:
bash
Copy code



   

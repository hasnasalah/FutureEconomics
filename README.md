# FutureEconomics
<h1>Macroeconomic Forecasting Project: GDP Growth and Unemployment Rate Predictions</h1>

<p style="font-size:14px">
In this project I aim to forecast and the predict the United States Gross Domestic Product (GDP) growth and unemployment rate based on historical macroeconomic data.
From GDP, Unemployment rates, Governement expenditure and import & export.
</p>
<h2>Goals</h2>
<ol>
   <li>Predict GDP Growth: Using historical data and macroeconomic factors, forecast future GDP growth in the U.S.</li>
   <li>Forecast Unemployment Rate: Predict fluctuations in the unemployment rate based on variables like inflation,GDP, Interest Rate and other economic indicators.</li>

<h2>Dataset Sources</h2>
<ul>
<li>The dataset contains historical data on GDP, unemployment rate, inflation, interest rates, and government spending for the U.S. from reliable sources such as the <strong>Federal Reserve Economic Data (FRED)</strong> and<strong> the Bureau of Economic Analysis (BEA).</strong></li>
<li>The data has been sourced from both public APIs and offline data files.</li>
</ul>

<h2>Data Analysis and Visualization</h2>
<h3>Rolling Mean/Moving Average</h3>
<h3>Correlation:</h3>
The correlation matrix is used to assess the linear relationships between pairs of economic indicators. Correlation values range from -1 to 1, where:
<ul>
<li>1 means a perfect positive correlation (both variables move in the same direction)</li>
<li>-1 means a perfect negative correlation (both variables move in opposite directions)</li>
<li>0 means no correlation (no predictable relationship).</li>
<strong>Why Use Correlation in this Project?</strong>

<h2>Tools and Technologies</h2>
<ul>
    <li>Programming Language: Python</li>
    <li>Data Analysis Libraries: pandas, numpy</li>
    <li>Visualization: matplotlib</li>
    <li>APIs: FRED API, BEA API (to pull real-time data)</li>
    <li>Database: SQLITE (for data storage and management)</li>
    <li>IDE: VS Code for code development </li>
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
Clone or download this repository to your local machine using the following url: <a href="https://github.com/hasnasalah/FutureEconomics.git">Economic Future Project</a>
<ul>
<li>Open Visual Studio Code and open the project folder.</li>
<li>Set up the Virtual Environment:</li>

<ul>
<li>Open the terminal in Visual Studio Code (View > Terminal).</li>
<li>Navigate to your project directory if not already there.</li>
<li>Create virtual envirenment using the folowing code:</li>
on Windows:
    python -m venv venv
on macOS/Linux:
python3 -m venv venv
<li> Activate the virtual envirenment</li>
   <ul>
   <li> On macOS/Linux using the following command:</li>
         source venv/bin/activate
   <li> On Windows using:</li>
        venv/scripts/activate
<li> Run the libraries<li>
Note: 
Ensure that you have the pip installed on your local machine to install the libraries using requirements file::
<strong>on macOS/Linux:</strong>
pip3 install -r requirements.txt
<strong> On windows:</strong>
  pip install -r requirements.txt






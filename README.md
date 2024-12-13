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
    </ol>

   <h2>Dataset Sources</h2>
   <ul>
   <li>The dataset contains historical data on GDP, unemployment rate, inflation, interest rates, and government spending for the U.S. from reliable sources such as  the <strong>Federal Reserve Economic Data (FRED)</strong> and<strong> the Bureau of Economic Analysis (BEA).</strong></li>
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
    </ul>
<strong>Why Use Correlation in this Project?</strong>

<h2>Tools and Technologies</h2>
<ul>
    <li>Programming Language: Python</li>
    <li>Data Analysis Libraries: pandas, numpy</li>
    <li>Visualization: matplotlib</li>
    <li>FRED API (to pull data)</li>
    <li>CVS file</li>
    <li>Database: SQLITE (for data storage and management)</li>
    <li>IDE: VS Code for code development </li>
</ul>
<h2>Features Used in the Project</h2>

<ul>
  <li>
    <strong>Data Cleaning and Preprocessing</strong>
    <ul>
      <li>Handled missing and invalid data by replacing <code>INF</code>, <code>-INF</code>, and <code>NA</code> with <code>NaN</code>.</li>
      <li>Filter data to get the last 20 years for analysis.</li>
      <li>Transf wide data into long one using the <code>melt()</code> method.</li>
    </ul>
  </li>
  <li>
    <strong>Data Storing</strong>
    <ul>
      <li>Use SQLite as the database to store cleaned Data.</li>
      <li>Create tables based on economic indicators(GDP,Inflation, etc..) using Python scripts.</li>
    </ul>
  </li>
  <li>
    <strong>Data Analysis and Visualization</strong>
    <ul>
      <li>Grouped data by year and calculated averages for global interest rate.</li>
      <li>Visualize interest rates over time using <code>Matplotlib</code>.</li>
      <li>Highlight Interest Rate for specific countries (United States, China) to compare approches.</li>
    </ul>
  </li>
  <li>
    <strong>Custom Functions</strong>
    <ul>
      <li>Reusable functions for database operations (<code>create_table</code>, <code>insert_into_table</code>).</li>
      <li>Reusable fetching , cleaning, and storing methods.</li>
    </ul>
  </li>
  <li>
    <strong>Project Structure</strong>
    <ul>
      <li>Organized the project into modules (<code>data_cleaning</code>, <code>create_database</code>),<code>data_visualization</code> notebook</li>
      <li>Included a virtual environment and requirements file.</li>
    </ul>
  </li>
  <li>
    <strong>Key Insights</strong>
    <ul>
      <li> Steady growth shown  but conistant increase of inflation and unemployment Rates.</li>
      <li>GDP shows steady growth, while government spending has varied, reflecting economic cycles<li>
      <li>Analyzed interest rate trends during major events (2008 financial crisis, Covid 19 pandemic).</li>
      <li>Highlighted differences in policy responses by key economies like the U.S. and China.</li>
    </ul>
  </li>
</ul>

<h2>Setup Instructions</h2>
<h3>Requirements:</h3>
<ul>
    <li>Python 3.6+</li>
    <li>Libraries: The following Python libraries are required:
    <ul>
        <li>pandas</li>
        <li>numpy</li>
        <li>matplotlib</li>
        <li> OS library (dotenv)</li>
    </ul>
</ul>
<h2>Clone the project:</h2>
  Clone or download this repository to your local machine using the following url: <a href="https://github.com/hasnasalah/FutureEconomics.git">Economic Future Project</a>
<h2>Run the project</h2>
<ul>
    <li>Open Visual Studio Code and open the project folder.</li>
    <li>Set up the Virtual Environment:</li>
    <ul>
        <li>Open the terminal in Visual Studio Code (View > Terminal).</li>
        <li>Navigate to your project directory if not already there.</li>
        <li>Create Virtual Environment using the folowing code:</li>
             <strong>on Windows:</strong>
               python -m venv venv
             <strong>on macOS/Linux:</strong>
             python3 -m venv venv
        <li> Activate the virtual environment</li>
             <ul>
                 <li> On macOS/Linux using the following command:</li>
                       source venv/bin/activate
                 <li> On Windows using:</li>
                      venv/scripts/activate
            </ul>
    </ul>
    
<li> Run the libraries<li>
    Note: Ensure that you have the pip installed on your local machine to install the libraries using requirements file:</br>
    <strong>on macOS/Linux:</strong></br>
            pip3 install -r requirements.txt</br>
    <strong> On windows:</strong></br>
            pip install -r requirements.txt</br>
<li>.env File Access</li>
The `.env` file is stored in a private repository. If you don't have access, Please Contact Hasna Ben Jillali
<li>Using the .env File</li>
After Cloning the .env repositry: The `.env` file should be placed in the root directory of the project.
<strong>Deactivate</strong>
          Make sure after finishing with the project Deactivate the virtual environment using deactivate commend
</ul>
<h3> Run The Code</h3>
<ol>
   <li>data_cleaning file</li>
         Using teminal run the following command:
         <ul><li>On Windows:</li>
          python data_cleaning.py
         <li> On macOS:</li>
          python3 data_cleaning.py
         </ul>
   <li>create_database file</li>
          Using teminal run the following command:
         <ul><li>On Windows:</li>
          python create_database.py
         <li> On macOS:</li>
          python3 create_database.py
         </ul>
      <li>data_visualization file</li>
          run using the run all tab in the vs code 
         </ul>

<h2>Project Summary:</h2>
<p>This project analyzes the United States economic indicators like interest rate, GDP, unemployment rate, governement spending and inflation over the last 20 years. The finding includes significant change in global interest rate, with a clear that it is rised in 2008 due to the financial crisis. After Covid-19 as well, global interest rate is stable around 5%, showing efforts to balance the economic. Comparison between China and the United States shows different approaches: China focused on  stability, while the U.S. follows an aggressive policy with negative real interest rate to stimulate the economy.</p>

<h3>Next Steps:</h3>
<p>I, am continuing to learn, keep exploring economic trends and update the analysis, adding additional data and advanced methods to enhance the analysis and predictions.</p>


    
         

    
       
      






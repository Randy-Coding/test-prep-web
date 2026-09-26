questions = {
    "Mathematical Preliminaries 1": {
        "In the dice experiment example, what are “outcomes” versus “events,” and why does probability focus on events?": "Outcomes are the individual results of an experiment, while events are sets of outcomes. Probability focuses on events because it allows us to calculate the likelihood of a group of outcomes occurring, rather than just one specific outcome.",
        "What is probability theory?": "Its an attempt to provide a formal framework for reasoning about the likelihood of events.",
        "What is an experiment": "A procedure which yields one set of possible outcomes.",
        "What is sample space?": "The set of possible outcomes of an experiment.",
        "What is an event?": "A subset of the sample space.",
        "What is the range of probabilities?": "The range of probabilities is from 0 to 1, inclusive.",
        "What is the sum of probabilities of all outcomes in a sample space?": "The sum of probabilities of all outcomes in a sample space is 1.",
        "What is the equation for the probability of an event?": "P(E) = the sum of the samples within its subset",
        "What is a random variable?": "A random variable is a function that assigns a numerical value to each outcome in a sample space.",
        "What is the difference between probability and statistics?": "Probability deals with predicting the likelihood of future events, while statistics involves analyzing data from past events. Also Probability is theoretical branch of mathematics on the consequences of definitions, while statistics is applied mathematics trying to make sense of real - world observations",
        "Events A and B are independent iff:": "P(A and B) = P(A) * P(B)",
        "Upside and downside to independence": "It makes calculations easier, but its bad for predicting things",
        "How is conditional probability defined": "P(A|B) = P(A and B) / P(B)",
        "What is Baye's Theorem": "P(A|B) = P(B|A) * P(A) / P(B)",
        "How is Baye's theorem helpful?": "It lets us reverse the direction of dependencies",
        "What does (A|B) mean in english": "The probability of A given B",
        "What are pdfs": "A proability density function. Its a representation of random variables as histograms",
        "What are cdfs": "Cumulative Distribution Function. It is a running sum of the a probability denisity function.",
        "What is descrptive statistics?": "A method to capture the properties of a given data set / sample.",
        "What is a central tendency measure?": "A descrption of the center of a dataset. Ex: mean, median, mode",
        "What is a variation or variability measure?": "Describes how spread out the data is. Ex: range, variance, standard deviation",
        "What is a geometric mean?": "The nth root of the product of n numbers. It is used to calculate the average rate of return over time.",
        "Relationship between geometric mean and arithmetic mean": "The geometric mean is always less than or equal to the arithmetic mean",
        "When to pick mean": "When the distributions are symmetric without major outliters: ex. height and weight",
        "when to pick median": "When the distribution is skewed or has outliers: ex. income",
        "Difference between population and sample standard deviation?": "Population SD divides by n, while sample SD divides by n-1. Where n is the number of data points.",
        "What do data scientists need to learn that computer scientists tend to not have to learn (as much)?": """
        Data visualization and storytelling
        Statistictal and probability theory
        Data cleaning and preprocessing
        Ability to ask interesting questions about what we can learn from data.
        """,
    },
    "Mathematical Preliminaries 2": {
        "What does it mean when X and Y are correlated?": "X has some predictive power over the value of Y",
        "What is the correlation coefficient?": "Measure of the degree to which Y is a function of X.",
        "Range of correlation coefficient?": "-1 to 1",
        "What does the Pearson Correlation measure?": "The linear relationship between two variables. It produces the correlation coefficient.",
        "What does the numerator of the Pearson Correlation Coefficient define?": "The covariance of X and Y",
        "What does it mean when you take r^2 of a correlation coefficient?": "It represents the proportion of variance in Y that is predictable from X.",
        "When measuring p value in correlation signficiance, what does p depend on?": "The value of r (how strong the correlation is) and the number of data points (n).",
        "How do you know if there's a good linear fit on f(x)?": "If the variance of f(x) is lower than the varaince of y",
        "When pick spearman rank correlation over pearson coefficient?": "When relationships are non-linear or when there outliers.",
        "What is the time complexity of the lag-k autocorrelation?": "O(n)",
        "What is the time complexity of the fast fourier transform (FFT)?": "O(n log n)",
        "Logarithim relationship to exponents": "Logarithms are the inverse of exponents.",
        "Example of log to exponent": "If log_b(x) = y, then b^y = x",
        "How are logs used in statistics?": "Summing logs of probabilities is more numerically stable than multiplying them",
        "Briefly discuss three roles or use cases of logarithms in analyzing and interpreting data": "Logarithms help compress large ranges of data, making it easy to visualize it. Logarithms convert exponential relationships into linear ones, which lets exponential growth or decay be analyzed with linear models. It helps measure relative change",
    },
    "Python for Data Science": {
        "What is the difference between BeautifulSoup and LXML?": "BeautifulSoup and LXML both parse XML and HTML documents, but LXML is generally faster and more efficient than BeautifulSoup. BeautifulSoup is more user-friendly and easier to use for beginners, while LXML offers more advanced features and better performance for larger documents.",
        "When would you pick BeuatifulSOup over XML or vice versa?": "Pick beautifulsoup when you prioritize ease of use. Pick LXML when you prioritize performance.",
        "What is the role of the requests library in retrieving web data?": "The lbrary you to make HTTP requests to websites, allowing you to download the content of the web pages.",
        "Name of a table in Pandas and an array in Pandas?": "Table: DataFrame, Array: Series",
        "What command lets you see the first few rows of a DataFrame?": "head()",
        "What command lets you see information like mean, std, and quartiles of a DataFrame?": "describe()",
        "What command lets you combine dataframe d1 and d2 together?": "pd.merge(d1,d2,on='common_column')",
        "What packages do you use for Text Data preprocessing?": "NLTK ",
        "What packages do you use for numeric data preprocessing?": "Pandas, NumPy",
        "What packages do you use for image data preprocessing?": "scikit-image",
        "Data preprocessing best practice?": "Preprocess data only once",
        "What are the 4 steps to data science with python?": "Get data, Data Pre-processing, Analysis and Modelling, Evaluate and Present",
        "What stack is most useful for analysis and modeling of data?": "The Scipy stack",
        "How do you define a matrix in Numpy?": "matrix = np.array([[x,y],[a,b]])",
        "How do you invert a matrix in Numpy?": "Inverted_Matrix = np.linalg.inv(matrix)",
        "What common functionality does Scipy offer?": "Linger Algebgra, Oprimization, Statistics, Singal Processing, Special functions",
        "What are the names of the Linger Algebgra, Oprimization, Statistics, Singal Processing, Special function functions?": "scipy.linalg, scipy.optimize, scipy.stats, scipy.signal, scipy.special",
        "What big features does Sympy offer": "Differentiation, Integraiton, simplifying equations, symbolic manipulation",
        "What is the big visualization choice for python": "matplotlib",
    },
    "Python for Data Science 2": {
"What is one goal of this lecture?": "Introduce the learning from data paradigm.",  # slide 2
"Is this course a full machine learning course?": "No.",  # slide 2

"What scientific question is used as an example?": "The laws governing the motion of planets.",  # slide 3

"What two measurements were observed for planets?": "Distance from the sun and orbital period.",  # slide 4

"What question arises from the planetary data?": "Can a law be derived from the observations?",  # slide 5

"Does the raw data look linear when plotted?": "No.",  # slide 6

"What transformation was proposed to make the data linear?": "Plot log(Time) vs log(Distance).",  # slide 7

"What happens to the data in a log-log plot?": "It looks approximately linear.",  # slide 8

"Why can't we just use two points to define a line?": "Because it does not fit all observations well.",  # slide 9

"What problem arises when using only two points?": "It fails to explain other data points like Jupiter and Saturn.",  # slide 10

"What is the least squares approach?": "Minimize total squared error over all observations.",  # slide 11

"What parameters define a line in least squares?": "Slope (a) and intercept (b).",  # slide 11

"What does least squares minimize?": "The sum of squared residuals.",  # slide 11

"What is a residual?": "The difference between observed and predicted values.",  # slide 12

"What was the result of applying least squares?": "A line with slope ~1.5 and intercept ~-0.1.",  # slide 13

"What law was derived from the regression?": "Kepler's Third Law.",  # slide 15

"What relationship was found between T and R?": "T^2 is proportional to R^3.",  # slide 15

"What is Tom Mitchell's definition of machine learning?": "A program learns from experience if its performance improves with experience.",  # slide 16

"What is machine learning fundamentally?": "Function approximation.",  # slide 17

"What types of models can extend beyond linear models?": "Polynomial and non-linear models.",  # slide 17

"What is the risk when using more complex models?": "Overfitting.",  # slide 18

"What library is highlighted for machine learning in Python?": "Scikit-learn.",  # slide 21

"What are two types of machine learning shown?": "Supervised and unsupervised learning.",  # slide 22

"What is classification?": "Assigning labels to data points.",  # slide 23
"What is clustering?": "Grouping similar data points without labels.",  # slide 23

"What tasks does scikit-learn support?": "Regression, classification, clustering, and dimensionality reduction.",  # slide 24

"What is a key caution when using machine learning tools?": "Understand the algorithms before applying them."  # slide 24
},
    "Assembling Data Sets": {
        "What is Data Munging / data wrangling": "Acquiring data and preparing it for analysis",
        "What do good data scientists spend most of their time doing?": "Cleaning and formatting data.",  # slide 2
        "Name one advantage of Python for data science.": "It has libraries and features like regular expressions for easier data munging.",  # slide 3
        "What is R primarily used for?": "Statistical programming.",  # slide 3
        "What are notebook environments useful for?": "Mixing code, data, computational results, and text.",  # slide 4
        "Name one property notebook environments help achieve.": "Reproducibility.",  # slide 4
        "What is a data pipeline?": "A sequence of processing steps from start to finish.",  # slide 5
        "Why should you design code for data pipelines carefully?": "Because you may need to redo your analysis from scratch.",  # slide 5
        "What data format is commonly used for tabular data?": "CSV.",  # slide 6
        "What data format is commonly used for APIs?": "JSON.",  # slide 6
        "What is a key difference between JSON and XML?": "JSON is more concise, while XML uses more verbose tag-based structure.",  # slide 71
        "What is the most critical issue in a modeling project?": "Finding the right dataset.",  # slide 81
        "What is metadata?": "Additional information about data such as titles, captions, or edit history.",  # slide 81
        "Name one source of data.": "Government datasets.",  # slide 91
        "Why is access to proprietary data often difficult?": "Because organizations usually do not allow outside access.",  # slide 10
        "What is Data.gov?": "A platform with hundreds of thousands of open government datasets.",  # slide 11
        "How can academic datasets be found?": "By searching papers and looking for open science or data releases.",  # slide 12
        "What is web scraping?": "Extracting data from web pages.",  # slide 13
        "What should you check before scraping a website?": "APIs and terms of service.",  # slide 13
        "What are two common ways to access online datasets?": "Bulk downloads and APIs.",  # slide 14
        "What is an example use of sensor data?": "Measuring traffic flows using GPS data.",  # slide 15
        "What is crowdsourcing in data collection?": "Using many people to gather or annotate data.",  # slide 16
        "What is sweat equity in data collection?": "Manually collecting or entering data.",  # slide 17
        "What does 'garbage in, garbage out' mean?": "Poor data quality leads to poor analysis results.",  # slide 18
        "Name one data cleaning issue.": "Outlier detection.",  # slide 18
        "What is the difference between errors and artifacts?": "Errors are lost or incorrect data, artifacts are systematic issues from processing.",  # slide 19
        "Why is having a preconception of results important?": "It helps detect anomalies or artifacts.",  # slide 20
        "What caused the artifact spike in PubMed author data?": "Switching to full first names in 2002.",  # slide 22
        "What is data compatibility?": "Making data consistent for valid comparisons.",  # slide 23
        "What is a common issue in unit conversions?": "Inconsistent units like cm, m, km.",  # slide 24
        "What is a Z-score?": "A dimensionless quantity used for normalization.",  # slide 24
        "What caused the Ariane 5 rocket failure?": "Incorrect numeric type conversion.",  # slide 25
        "What is name unification?": "Standardizing different representations of the same name.",  # slide 26
        "What time standard is recommended for data alignment?": "UTC.",  # slide 27
        "What is one method for financial data comparison?": "Using percentage returns instead of absolute prices.",  # slide 28
        "Why is setting missing values to zero often incorrect?": "Because it misrepresents unknown data.",  # slide 29
        "What is imputation?": "Estimating missing values.",  # slide 30
        "Name one imputation method.": "Mean value imputation.",  # slide 31
        "What is an outlier?": "A value significantly different from others in the dataset.",  # slide 32
        "Why should outliers be investigated instead of immediately deleted?": "Because they may indicate errors or important patterns.",  # slide 32
        "How can outliers be detected in high dimensions?": "By identifying points far from cluster centers.",  # slide 33
        "When can deleting outliers improve a model?": "When they are measurement errors.",  # slide 34
        "When can deleting outliers harm a model?": "When they represent valid but unexplained data.",  # slide 34
    },
    "Statistical Distribution": {
        "What is the relationship between statistics and data science according to the quote?": "A data scientist knows more statistics than a computer scientist and more computer science than a statistician.",  # slide 2
        "What are the two main branches shown in the central dogma of statistics?": "Descriptive statistics and inferential statistics.",  # slide 3
        "What is a statistical distribution?": "The frequency or probability distribution of a random variable.",  # slide 4
        "Name one common statistical distribution.": "Normal distribution.",  # slide 4
        "Why are classical distributions important?": "They often occur in practice and have known formulas and statistical tests.",  # slide 5
        "Does data always follow a classical distribution just because it looks similar?": "No.",  # slide 5
        "What defines a binomial distribution?": "n independent trials with two outcomes and probabilities p and 1-p.",  # slide 6
        "What are the parameters of a binomial distribution?": "n and p.",  # slide 6
        "What is the shape of a binomial distribution?": "Discrete and often bell-shaped.",  # slide 7
        "What does P(X = x) represent in a binomial distribution?": "The probability of exactly x successes in n trials.",  # slide 6
        "What range of values can the sum of two dice take?": "Integers from 2 to 12.",  # slide 9
        "What is the normal distribution?": "A continuous bell-shaped distribution defined by mean and standard deviation.",  # slide 10
        "What are the parameters of a normal distribution?": "Mean (mu) and standard deviation (sigma).",  # slide 10
        "What happens to the binomial distribution as n approaches infinity?": "It approaches a normal distribution.",  # slide 11
        "What kind of data is often normally distributed?": "Experimental error.",  # slide 11
        "What is a Z-score used for?": "Measuring how far a value is from the mean in standard deviations.",  # slide 12
        "Are all bell-shaped distributions normal?": "No.",  # slide 13
        "Give an example of a non-normal distribution.": "Log-normal distribution of stock returns.",  # slide 13
        "What type of distribution models lifespan with probability p of surviving each day?": "Geometric-like distribution where Pr(n) = p^(n-1)(1-p).",  # slide 14
        "What does the Poisson distribution measure?": "The frequency of rare events in a fixed interval.",  # slide 15
        "What parameter defines the Poisson distribution?": "Mean mu.",  # slide 15
        "Give an example of a Poisson process.": "Number of lightbulb burnouts per day.",  # slide 16
        "What distribution can model number of kids per family under repeated decisions?": "Poisson distribution.",  # slide 17
        "What is a power law distribution?": "A distribution of the form p(x) = c x^-a.",  # slide 18
        "What is a key property of power law distributions?": "Large values occur rarely but consistently.",  # slide 18
        r"What is the 80-20 rule?": r"20% of X accounts for 80% of Y.",  # slide 18
        "Why do city populations follow power laws instead of normal distributions?": "Because large values are much more extreme than normal distribution predictions.",  # slide 19
        "How can you identify a power law distribution visually?": "It appears as a straight line on a log-log plot.",  # slide 20
        "What happens to probability when x doubles in a power law?": "It decreases by a factor of 2^a.",  # slide 23
        "Give one real-world example of a power law.": "Word frequencies.",  # slide 24
        "What is Zipf's law?": "The kth most popular word occurs with frequency proportional to 1/k.",  # slide 25
        "Why is the mean not useful in power law distributions?": "Because extreme values dominate and distort it.",  # slide 27
        "What statistic is more useful than the mean for power laws?": "Median.",  # slide 27
        "What does scale invariance mean in power law distributions?": "Zoomed-in portions look similar to the whole distribution.",  # slide 27
    },
    "Statistical Significance":
    {
    "What is statistical significance?": "A measure of whether an observed effect is likely due to chance or not.",  # slide 2

    "What is the null hypothesis?": "The assumption that there is no effect or no difference.",  # slide 3
    "What is the alternative hypothesis?": "The assumption that there is an effect or difference.",  # slide 3

    "What does a p-value represent?": "The probability of observing results at least as extreme as the data assuming the null hypothesis is true.",  # slide 4

    "What is a significance level (alpha)?": "A threshold used to decide whether to reject the null hypothesis.",  # slide 5

    "When do you reject the null hypothesis?": "When the p-value is less than alpha.",  # slide 5

    "What is a Type I error?": "Rejecting the null hypothesis when it is actually true.",  # slide 6
    "What is a Type II error?": "Failing to reject the null hypothesis when it is false.",  # slide 6

    "What does statistical power measure?": "The probability of correctly rejecting a false null hypothesis.",  # slide 7

    "What is a confidence interval?": "A range of values that likely contains the true population parameter.",  # slide 8

    r"What does a 95% confidence interval mean?": r"If repeated many times, 95% of such intervals would contain the true parameter.",  # slide 8

    "What is sampling variability?": "The natural variation in sample statistics across different samples.",  # slide 9

    "Why do we use random sampling?": "To ensure samples are representative of the population.",  # slide 10

    "What is bias in sampling?": "Systematic deviation from the true population value.",  # slide 11

    "What is a large sample size effect?": "Larger samples reduce variability and increase reliability of estimates.",  # slide 12

    "What is a test statistic?": "A value calculated from sample data used to evaluate the null hypothesis.",  # slide 13

    "What is a z-test used for?": "Testing hypotheses about means when population variance is known.",  # slide 14

    "What is a t-test used for?": "Testing hypotheses about means when population variance is unknown.",  # slide 15

    "What happens to the t-distribution as sample size increases?": "It approaches the normal distribution.",  # slide 15

    "What is multiple testing problem?": "Performing many tests increases the chance of false positives.",  # slide 16

    "What is p-hacking?": "Manipulating analysis to obtain statistically significant results.",  # slide 17

    "Why is statistical significance not equal to practical significance?": "A result can be statistically significant but have a very small or unimportant effect.",  # slide 18

    "What is correlation?": "A measure of association between two variables.",  # slide 19

    "Does correlation imply causation?": "No.",  # slide 19

    "What is an example of a confounding variable?": "A variable that influences both variables being studied.",  # slide 20

    "What is Simpson's paradox?": "A trend that appears in groups reverses when groups are combined.",  # slide 21

    "Why is data visualization important in significance testing?": "It helps reveal patterns, outliers, and misleading results.",  # slide 22

    }
,
    "Building models": {
"What is modeling in data science?": "Encapsulating information into a tool that can make forecasts or predictions.",  # slide 2
"What are the three key steps in modeling?": "Building, fitting, and validating the model.",  # slide 2

"What is Occam's Razor?": "The principle that the simplest explanation is best.",  # slide 4
"How does Occam's Razor apply to models?": "It favors models with fewer parameters.",  # slide 4

"What is underfitting?": "A model with high bias that is too simple to capture patterns.",  # slide 5
"What is overfitting?": "A model with high variance that fits noise in the training data.",  # slide 6

"What is bias in modeling?": "Error from incorrect assumptions, often from overly simple models.",  # slide 8
"What is variance in modeling?": "Error from sensitivity to small changes in training data.",  # slide 8

"What is the goal of the bias-variance tradeoff?": "To balance model complexity to minimize total error.",  # slide 9

"What is one principle from Nate Silver?": "Think probabilistically.",  # slide 10
"What should models do when new information arrives?": "Update their forecasts.",  # slide 10

"What should good models output instead of a single prediction?": "A probability distribution over outcomes.",  # slide 11

"What are three properties of probabilities?": "They sum to 1, are non-negative, and rare events are not zero.",  # slide 12

"What function maps scores to probabilities?": "The logistic (sigmoid) function.",  # slide 13

"What is a live model?": "A model that updates predictions as new data arrives.",  # slide 14

"What is the purpose of looking for consensus in models?": "To compare forecasts and improve reliability.",  # slide 15

"What is boosting?": "A technique that combines multiple classifiers into an ensemble.",  # slide 15

"What was Google Flu Trends based on?": "Query frequency of illness-related search terms.",  # slide 16
"Why did Google Flu Trends fail?": "Changes in search behavior due to suggestions broke the model.",  # slide 16

"What does Bayes' theorem allow you to do?": "Update probabilities based on new evidence.",  # slide 17

"What are the three components of Bayesian reasoning?": "Prior, likelihood, and posterior.",  # slide 18

"Why can a positive medical test still mean low probability of disease?": "Because the prior probability may be very low.",  # slide 19

"Why is Bayesian reasoning useful in data science?": "It combines prior knowledge with observed data.",  # slide 20

"What is one step in building effective models?": "Develop baseline models.",  # slide 21
"What is another step in building effective models?": "Test with out-of-sample predictions.",  # slide 21

"What are first-principle models?": "Models based on theoretical understanding of a system.",  # slide 22
"What are data-driven models?": "Models based on observed data relationships.",  # slide 22

"What is a baseline model?": "A simple model used for comparison.",  # slide 23

"Give one example of a baseline model.": "Always predicting the most common label.",  # slide 24

"Name one dimension in the taxonomy of models.": "Linear vs non-linear.",  # slide 25

"What is a linear model?": "A model where the relationship is a straight line.",  # slide 26
"What is a non-linear model?": "A model with more complex relationships.",  # slide 26

"What is a general model?": "A model that uses only data without domain-specific assumptions.",  # slide 27
"What is an ad hoc model?": "A model built using domain knowledge.",  # slide 27

"What is a descriptive model?": "A model that explains its decisions.",  # slide 28
"What is a black-box model?": "A model whose internal logic is not easily interpretable.",  # slide 28

"What is an example of a descriptive model?": "Decision tree.",  # slide 29

"How do you apply a decision tree to test data?": "Start at the root and follow splits based on feature values.",  # slide 30

"What are levels of modeling?": "Breaking problems into sub-models at different levels.",  # slide 31

"What is hierarchical decomposition?": "Structuring models into subproblems for clarity and evaluation.",  # slide 32

"What are the four outcomes of a binary classifier?": "TP, TN, FP, FN.",  # slide 33

"What is accuracy?": "The ratio of correct predictions to total predictions.",  # slide 35

"What is precision?": "TP divided by TP plus FP.",  # slide 36

"What is recall?": "TP divided by TP plus FN.",  # slide 37

"What is the F-score?": "The harmonic mean of precision and recall.",  # slide 38

"Why is accuracy misleading in imbalanced datasets?": "Because predicting the majority class can give high accuracy.",  # slide 39

"What does an ROC curve show?": "The tradeoff between true positive rate and false positive rate.",  # slide 40

"What is a confusion matrix?": "A table showing prediction errors across classes.",  # slide 41

"What is absolute error?": "The difference between predicted and actual values.",  # slide 43
"What is relative error?": "The error divided by the actual value.",  # slide 43

"What is MSE?": "Mean squared error of predictions.",  # slide 43
"What is RMSE?": "The square root of mean squared error.",  # slide 43

"What is out-of-sample evaluation?": "Testing on data not used during training.",  # slide 44

"What is cross-validation?": "Training on subsets of data and averaging results.",  # slide 45
"What is leave-one-out validation?": "A form of cross-validation using all but one data point each time."  # slide 45
},
"Homework 1": {"Give one role of logarithms in data analysis.": "Transforming non-linear relationships into linear ones.",  # Q3
"Why are logarithms useful for large-scale data?": "They compress wide-ranging values.",  # Q3

"What is causation?": "A relationship where one variable directly affects another.",  # Q4
"What is covariance?": "A measure of how two variables change together.",  # Q5

"What does a positive Pearson correlation indicate?": "As one variable increases, the other increases.",  # Q5
"What does a negative Pearson correlation indicate?": "As one variable increases, the other decreases.",  # Q5
"What does the magnitude of Pearson r indicate?": "Strength of the linear relationship.",  # Q5
},
"Homework 2": {
    "What is probability concerned with?": "Predicting outcomes given a known model.",  # Q2
"What is statistics concerned with?": "Inferring models from observed data.",  # Q2

"Can you compute P(A and B) knowing only P(A) and P(B)?": "No.",  # Q2
"What is P(A and B) if A and B are independent?": "P(A) * P(B).",  # Q2
"What is P(A or B) if A and B are independent?": "P(A) + P(B) - P(A)P(B).",  # Q2
"What is P(A|B) if A and B are independent?": "P(A).",  # Q2
"What function is used to load CSV data in pandas?": "read_csv().",  # Q4
"What function shows the first rows of a DataFrame?": "head().",  # Q4

"What structure does JSON support that CSV does not?": "Hierarchical nesting.",  # Q4
"What is one advantage of XML over CSV?": "It supports structured hierarchical data.",  # Q4
"What condition allows Binomial to approximate Normal?": "Large n with p not near 0 or 1.",  # Q5
"What is the mean of the Normal approximation of Binomial?": "np.",  # Q5
"What is the variance of the Normal approximation of Binomial?": "np(1-p).",  # Q5
"What condition allows Binomial to approximate Poisson?": "Large n and small p with np ≈ λ.",  # Q5
"What is λ in the Poisson approximation?": "np.",  # Q5

"What type of distribution is Binomial?": "Discrete.",  # Q5
"What type of distribution is Poisson?": "Discrete.",  # Q5
"What type of distribution is Normal?": "Continuous."  # Q5
},
"Midterm 1": {
"What is Spearman correlation equivalent to?": "Pearson correlation on ranked data.",  # Q1
"When is geometric mean preferred?": "When dealing with multiplicative data like growth rates.",  # Q2

"Name one function in pandas.": "read_csv().",  # Q3
"What is one capability of pandas?": "Group-by operations.",  # Q3

"Name a library used for getting data.": "BeautifulSoup.",  # Q4
"Name a library used for modeling.": "Scikit-learn.",  # Q4

"Give one example of a sensor dataset.": "GPS tracking data.",  # Q5
"What insight can GPS data provide?": "Driving patterns.",  # Q5

"What is one advantage of NumPy?": "Fast array operations.",  # Q6
"What is one advantage of SciPy?": "Optimization tools.",  # Q6

"Which correlation should be used for ranked data?": "Spearman.",  # Q7

"What is SymPy used for?": "Symbolic math.",  # Q8
"Give one task SymPy can perform.": "Symbolic differentiation.",  # Q8

"What type of data is autocorrelation used for?": "Time series data.",  # Q9

"What does the requests library do?": "Fetch web page content.",  # Q10
"What does BeautifulSoup do?": "Parse HTML.",  # Q10

"What is Bayes' theorem used for?": "Updating probabilities with new evidence.",  # Q11
"What is P(jelly | peanut butter)?": "P(jelly and peanut butter) / P(peanut butter).",  # Q11

"What is used to measure relationship strength between hours studied and scores?": "Pearson correlation.",  # Q12
"What does a high r^2 value indicate?": "Strong predictive power.",  # Q12

"Is number of steps a random variable?": "Yes.",  # Q13
"Is number of steps discrete or continuous?": "Discrete.",  # Q13
"Is distance walked discrete or continuous?": "Continuous.",  # Q13

"Name one confounding factor in studying vs performance.": "Sleep."  # Q14
},
"Quiz 1 review": {
"Does the CDF contain more information than the PDF?": "False.",  # Q1
"Name one thing Google Ngram can analyze.": "Word usage trends over time.",  # Q2

"Give one example of a sample space outcome for two dice.": "(1,1).",  # Q3

"Name one centrality measure.": "Mean.",  # Q4
"Name another centrality measure.": "Median.",  # Q4

"What is one question you can ask about time series energy data?": "Is there seasonality?",  # Q5
"What is another question for time series data?": "Is there a daily pattern?",  # Q5

"What does probability focus on?": "Predicting future outcomes.",  # Q6
"What does statistics focus on?": "Analyzing past data.",  # Q6

"Give one real-world application of data science.": "Inventory management.",  # Q7
"Give another application of data science.": "Disease prediction.",  # Q7

"When are two events independent?": "When P(A and B) = P(A)P(B).",  # Q8

"What is Bayes' theorem formula?": "P(A|B) = (P(B|A)P(A)) / P(B).",  # Q9

"Name one skill a data scientist should develop.": "Curiosity.",  # Q10
"Name another skill a data scientist should develop.": "Ability to ask good questions."  # Q10
},
}

ALU Machine Learning – Formative 3

Probability Distributions, Bayesian Probability, and Gradient Descent Implementation

Overview

This repository contains the implementation of Formative 3 for the Machine Learning module. The project bridges the gap between theoretical mathematics and computational machine learning by implementing core statistical models, Bayesian probability, and optimization algorithms entirely from scratch, without the use of high-level ML abstractions.

Project Architecture

Part 1: Bivariate Normal Distribution (From Scratch)

Code: Probability_Distributions_ML_Formative_3.ipynb

Dataset: iris.csv (Features: Sepal Length & Sepal Width).

Implementation: * Extracted and preprocessed target variables.

Computed standard deviation, covariance, and correlation matrices natively.

Engineered a custom Bivariate Normal Probability Density Function (PDF).

Visualization: Generated contour plots to represent data distribution and 3D surface plots to visualize the probability surface, demonstrating the mathematical impact of mean, variance, and covariance on distribution geometry.

Part 2: Bayesian Sentiment Analysis

Code: Bayesian (2).ipynb

Dataset: Movie Review Dataset.

Implementation:

Conducted text preprocessing and exploratory data analysis (EDA).

Extracted and mapped positive and negative word frequencies.

Implemented a Naive Bayes classifier from scratch to calculate prior and posterior probabilities.

Categorized reviews based on maximum likelihood estimation (MLE).

Part 3: Mathematical Derivation of Gradient Descent

Documentation: Part 3 - Gradient Manual Calculation .pdf

Implementation: * Performed manual forward pass calculations for a linear regression model.

Derived the Mean Squared Error (MSE) loss function analytically using the Chain Rule.

Calculated gradients and executed manual parameter updates for 4 continuous iterations.

See attached PDF for complete mathematical proofs and derivations.

Part 4: Custom Gradient Descent Implementation (Python)

Code: part_4_gradient_descent.ipynb

Implementation:

Translated the mathematical derivations from Part 3 into Python using NumPy for vectorized operations.

Built the Gradient Descent optimization loop from scratch (zero reliance on scikit-learn or similar libraries).

Tracked loss convergence and parameter updates across epochs to validate the manual mathematical model.

Repository Structure

├── Bayesian (2).ipynb                                  
├── Probability_Distributions_ML_Formative_3.ipynb      
├── part_4_gradient_descent.ipynb                        
├── iris.csv                                           
├── Part 3 - Gradient Manual Calculation .pdf           
└── README.md                                           


Team & Contributions (Group 2)

Hikma Hamza (Team Lead): Project management, Git branch oversight, code review, mathematical validation, and documentation.

Sam Rurangamirwa: Lead developer for Python Gradient Descent (Part 4), data visualization architecture (Contour/3D plots), and manual derivations.

Dan Dushime: Lead developer for Bayesian Sentiment Analysis (Part 2), text dataset preprocessing, predictive probability computations, and manual derivations.

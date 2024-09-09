# ANOVA Study on Data Science Expertise

## Project Overview

This project investigates how university training and subsequent practical experience affect expertise in data science. The study includes undergraduate students, postgraduate trainees, and experienced data scientists. A knowledge test and case studies were used to assess data science competence, and ANOVA (Analysis of Variance) was applied to compare the groups, followed by post hoc tests for further analysis.

## Dataset

- **Participants**: 
  - Novice undergraduate students
  - Intermediate undergraduate students
  - Advanced undergraduate students
  - Postgraduate trainees
  - Experienced data scientists
- **Competence Score**: Composite score based on knowledge tests and case study evaluations.
- **Sample Size**: 100 participants (20 per group).

## Objectives

1. Determine whether there are significant differences in data science competence among the different participant groups.
2. Identify trends in competence across educational levels and practical experience.
3. Conduct pairwise comparisons to see how the groups differ from each other.

## Analysis

### Steps:
- **Outlier Detection**: Used z-scores to identify extreme values.
- **Assumptions Testing**:
  - **Normality**: Checked using histograms and the Shapiro-Wilk test.
  - **Linearity**: Visualized using scatter plots.
  - **Homogeneity of Variance**: Tested with Levene’s test.
- **ANOVA**: Conducted to test for significant differences across groups.
- **Post Hoc Analysis**: Uncorrected t-tests and Bonferroni-adjusted tests for pairwise comparisons.
- **Effect Size**: Calculated using η² (eta-squared) and Cohen's d for group differences.

### Results:
- The **ANOVA test** was statistically significant (**p < 0.001**), indicating that there are differences in competence between participant types.
- **Post Hoc Tests** revealed the specific groups that differ significantly from each other.

## Conclusion

The analysis shows that practical experience and advanced university training significantly improve data science competence. 

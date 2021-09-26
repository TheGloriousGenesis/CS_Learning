# Machine Learning

## Glossary

| Word | Definition|
|:----:|:---------:|
| Recommendation Systems | Predict what the user might enjoy watching or buying |
| Association rule learning (Affinity Analysis) | Unsupervised learning technique that only works with categorical data |
| Support (Affinity Analysis) | The frequency of the pattern given by the rule |
| Confidence (Affinity Analysis) | The strength of an association rule relating to the likelihood of customer buying item A, given item B |
| Lift (Affinity Analysis) | The interestingness of a rule by checking the strength of rule over random co-occurrence if two items | 

## Overview

- Driven by Industry need
- Top 10 websites in internet retailer 500 use it.

## Applications

- Amazon : Track purchase habits of products
- Ticket merchants : Tracks movies/theatres seen
- Social : Tracks blogs you've read and suggest threads, 
- Professional Social : Uses current job role to recommend roles

## Types of Recommendation Systems

A system that recommends for sales purposes is different to one that recommends for education purposes.
System type can be driven by experts or by different users. Personalisation level of the algorithm
can appear in the following way:
- <em><strong>Generic</strong></em> (all users get same recommendation)
- <em><strong>Targeted</strong></em> (based on type of category the user falls into e.g age, income ..)
- <em><strong>Transient</strong></em> (based on recent tracked behaviour of user)
- <em><strong>Persistent</strong></em> (based on long term tracked behaviour - preferences)

Recommendation systems have dependencies and in order to utilise the systems. 
- Availability of data (The strength of the system depends on the amount of data that can be used for the prediction)
- Privacy Issues (Sometimes we do not want to collect data on multiple devices or whilst doing additional activities)
  - Personal Information and identity
  - Purpose of collection information
  - Security
- Trustworthiness (Systems can be made to sell items that are more profitable, or reduce the recommendations on items they know you will pick anyways)
  - Incentives
  - Biases
  - Manipulation

### Type 1: Non-Personalized: Association Rule Learning

- Works well with small datasets, small customer 
- Find patterns between items that occur together
- Capture patterns in the form:
  - If <strong><span style="color:red">antecedent</span></strong>, then <strong><span style="color:green">consequent</span></strong> <br>
   Example: If (customer buys) <strong><span style="color:red"> tortillas and jalapenos </span></strong> then customer buys <strong><span style="color:green"> beans and avocados</span></strong>
- Metrics used : Support

This is calculated by:

$$
s(A \Rightarrow B) = P (A\ \cap \ B) = s(B \Rightarrow  A)
\\
s(A \Rightarrow B) = \frac{no. \ transactions \ with \ A \ and \ B}{no. \ total \ transactions}
$$

The higher the support the more popular item bundle is and vice versa. Low support should not be used unless need to know 
item frequency


- Metrics used : Confidence
  - used to see the strength of relations between items in groups. Does not work for high frequency items as those items are not
    necessarily linked to each other (e.g buying sugar and phone credit at tesco doesn't mean sugar will be used for credit). Better
    used for low occurring items.
- Metrics used : Lift
  - A lift > 1 means items A and item B appear more often together than expected (positive association)
  - A lift < 1 means items A and item B appear less often than together expected (negative association)
  - A lift ~ 1 means items A and item B appear almost as often together as expected (no link)

- Use Metrics with caution
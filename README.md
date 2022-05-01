## Chess Classifier Project
# Overview
Chess is a complex game that has been played by people for thousands of years. There are endless combinations of moves and strategies that lead to an exciting and unpredictable event. This is why it has had such longevity, and it is still enjoyed by people to this day. While many people do enjoy playing chess, another activity that people engage in is Chess Betting, or trying to bet on the outcome of a match before it is played. This is the problem we decided to address in our project.
# Business and Data Understanding
In order to tackle this problem, we decided to localize the problem to matches which are usually bet on, professional matches by Grand Masters. We accessed data from Chess.com on 1,500 matches played by renowned chess Grand Master Magnus Carlsen. This data included information about the opening moves played, the rating of each player, the color each player played as, etc.
# Modeling
We chose to go with a Random Forest model. This model proved to have the best results, after attempting a K-Nearest Neighbof and Decision Tree. After tuning our Random Forest model, we successfully created a model that could make meaningful predictions.
# Evaluation
Given the accuracy score of 0.74 and the recall score of 0.81 on losses, we can confidently say that our model will help bettors reliably pick Magnus's losses, helping them win these bets.
# Conclusion
Our model is able to reliably make meaningful predictions. For our next steps, we will be incorporating more data from different games and players, as well as focusing on more predictive data, such as players' accuracy score (a metric measuring players' moves in comparison to a computer that calculates the best possible move).

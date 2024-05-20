
<a name="readme-top"></a>



[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/alexzhaoo/nbaprediction">
    <img src="nba.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">NBA Rookie to All-Star Classifier</h3>

  <p align="center">
    This is a binary classification project based on stats from rookie players in the NBA. Given the first or second season of an NBA player, will they become an all-star?
    <br />
    <a href="https://github.com/alexzhaoo/nbaprediction"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>

## Project Description

This project, titled **NBA Rookie to All-Star Classifier**, aims to predict whether a rookie NBA player will become an all-star based on their first or second season box score. Utilizing an artificial perceptron for binary classification, the model leverages linear algebra techniques to update weight vectors iteratively during training. Principal Component Analysis (PCA) is employed to reduce the dimensionality of the feature set. The final weight vectors, representing the trained model, are saved for future predictions, allowing the classifier to be reused without retraining. 

## Customizing the Model

Users can easily download the code from the [GitHub repository](https://github.com/alexzhaoo/nbaprediction) and experiment with different parameters to see how they affect the model's accuracy. To change the maximum iterations and the learning rate (`eta`), users can modify the `imax` and `eta` parameters within the `perceptronLearningRule` function. For instance, in the  code, `imax` is set to 15,000 and `eta` is set to 0.001. Users can adjust these values to see how increasing or decreasing the number of iterations or the learning rate impacts the performance and accuracy of the classifier.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/alexander-zhao-926225211/

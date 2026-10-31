library(tidyr)
library(ggplot2)

students <- data.frame(
  student = c("reethu", "deepu", "krishna", "priya", "raja"),
  math = c(99, 98, 97, 96, 95),
  science = c(100, 68, 79, 89, 90),
  english = c(56, 78, 90, 78, 99),
  hours = c(1, 2, 3, 4, 5)
)

# Convert data from wide to long format
long_df <- pivot_longer(
  students,
  cols = c(math, science, english),
  names_to = "subject",
  values_to = "score"
)

# Calculate average scores
avgs <- colMeans(students[, c("math", "science", "english")])

# Bar chart
barplot(
  avgs,
  main = "Average Subject Scores",
  xlab = "Subject",
  ylab = "Average Score",
  col = c("#3498db", "#2ecc71", "#e74c3c"),
  ylim = c(0, 100),
  border = "black"
)

# Add overall average line
abline(
  h = mean(avgs),
  col = "darkgray",
  lty = 2
)

# Add legend
legend(
  "topright",
  legend = paste("Overall avg:", round(mean(avgs), 1)),
  lty = 2,
  col = "darkgray"
)

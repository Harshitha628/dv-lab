library(tidyr)
library(ggplot2)

students <- data.frame(
  student = c("reethu", "deepu", "krishna", "priya", "raja"),
  math = c(99, 98, 97, 96, 95),
  science = c(100, 68, 79, 89, 90),
  english = c(56, 78, 90, 78, 99),
  hours = c(1, 2, 3, 4, 5)
)

head(students)

long_df <- pivot_longer(
  students,
  cols = c(math, science, english),
  names_to = "subject",
  values_to = "score"
)

ggplot(long_df, aes(x = student, y = score, fill = subject)) +
  geom_bar(stat = "identity", position = "dodge") +
  scale_fill_brewer(palette = "Set1") +
  labs(
    title = "Scores by Student and Subject",
    x = "Student",
    y = "Scores"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

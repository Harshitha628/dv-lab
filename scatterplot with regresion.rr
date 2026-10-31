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

ggplot(students, aes(x = hours, y = math, label = student)) +
  geom_point(aes(color = math), size = 4) +
  geom_smooth(
    method = "lm",
    se = TRUE,
    color = "steelblue",
    linetype = "dashed"
  ) +
  geom_text(vjust = -1, size = 3) +
  scale_color_gradient(low = "orange", high = "darkblue") +
  labs(
    title = "Hours Studied vs Math Score",
    x = "Hours Studied",
    y = "Math Score"
  ) +
  theme_minimal()

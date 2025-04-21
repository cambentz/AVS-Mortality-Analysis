data <- read.csv("165+PRA+PAC.csv")

mean_sbp <- mean(data$SBP, na.rm = TRUE)
mean_dbp <- mean(data$SBP, na.rm = TRUE)

sbp_count <- sum(!is.na(data$SBP))
dbp_count <- sum(!is.na(data$DBP))

bp_counts <- data.frame(
  Type = c("SBP", "DBP"),
  Count = c(sbp_count, dbp_count)
)

blood_pressure_summary <- data.frame(
  Type = c("SBP", "DBP"),
  Value = c("mean_sbp", "mean_Ddbp")
)

library(ggplot2)

ggplot(blood_pressure_summary, aes (x = Type, y = Value, fill = Type)) +
  geom_bar(stat= "identity", width = 0.5) +
  labs(title = "mean SBP and DBP", y = "Blood pressure (mmHg)", x = "") +
  theme_minimal()



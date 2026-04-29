library(readxl)
library(ggplot2)

# Load dataset
getwd()
setwd("D:/optimization project")
df <- read_excel("Data_Train.xlsx")

#Histogram
p1 <- ggplot(df, aes(x = Price)) +
  geom_histogram(bins = 50) +
  labs(
    title = "Distribution of Ticket Prices",
    x = "Ticket Price",
    y = "Frequency"
  )
p1

#Boxplot
p2 <- ggplot(df, aes(x = Airline, y = Price)) +
  geom_boxplot() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
  labs(
    title = "Ticket Price Distribution by Airline",
    x = "Airline",
    y = "Ticket Price"
  )
p2


ggsave("price_histogram.png", plot = p1, width = 7, height = 5, dpi = 300)
ggsave("price_boxplot_airline.png", plot = p2, width = 9, height = 6, dpi = 300)

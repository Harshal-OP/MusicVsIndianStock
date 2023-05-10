library(tidyverse)
library(ggplot2)
library(lubridate)


# Reading the csv file
stock_data <- read.csv("NSEI.csv")

# Converting the Date column to Date format
stock_data$Date <- mdy(stock_data$Date)


# Plotting the relation between Weighted Average of Song Valence and Change in Stock Price
ggplot(data = stock_data, aes(x = wtAVG, y = ChangeStock)) +
  geom_point(aes(colour = Date)) +
  labs(title = "Weighted Average of Song Valence vs Change in Stock Price", 
       x = "Weighted Average of Song Valence",
       y = "Change in Stock Price") +
  theme_bw()


# Plotting the Relation Between Weighted Average of Song Valence and Change in Stock Price

ggplot(data = stock_data, aes(x = wtAVG, y = ChangeStock)) +
  geom_point(aes(colour = Date)) +
  labs(title = "Weighted Average of Song Valence vs Change in Stock Price", 
       x = "Weighted Average of Song Valence",
       y = "Change in Stock Price") +
  theme_bw()

# Plotting the Time Series Graph
ggplot(data = stock_data, aes(x = Date, y = wtAVG)) +
  geom_line(aes(colour = "Music Sentiment")) +
  geom_line(aes(y = ChangeStock, colour = "Change in Stock Price")) +
  labs(title = "Time Series Graph of Music Sentiment vs Change in Stock Price", 
       x = "Date",
       y = "Value") +
  theme_bw()


# Creating the linear model
lm_model <- lm(ChangeStock ~ wtAVG, data = stock_data)

# Plotting the linear model
ggplot(data = stock_data, aes(x = wtAVG, y = ChangeStock)) +
  geom_point(aes(colour = Date)) +
  geom_smooth(method = lm, se = FALSE) +
  labs(title = "Weighted Average of Song Valence vs Change in Stock Price", 
       x = "Weighted Average of Song Valence",
       y = "Change in Stock Price") +
  theme_bw()


# Summary of the linear model
summary(lm_model)



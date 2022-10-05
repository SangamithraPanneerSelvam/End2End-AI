
dataset<-read.csv('C:/Users/Sangamithra/Desktop/project/Wedding/3.Uploading/processed_data.csv')
dataset



#Categorical Encoding

encode_ordinal <- function(x, order = unique(x)) {
  x <- as.numeric(factor(x, levels = order, exclude = NULL))
  x
}

dataset[["Season_encoded"]] <- encode_ordinal(dataset[["Season"]])
dataset[["Wedding_destination_encoded"]] <- encode_ordinal(dataset[["Wedding_destination"]])
dataset[["Location_encoded"]] <- encode_ordinal(dataset[["Location"]])
dataset[["Priority_1_encoded"]] <- encode_ordinal(dataset[["Priority_1"]])
dataset

wedding_data=dataset[ , c("Season_encoded", "Wedding_destination_encoded","Location_encoded","Priority_1_encoded","Guest_number","Total_Estimate")] 

#Splitting dataset into Training and testing data
install.packages('caTools')
library(caTools)
set.seed(42)
split=sample.split(wedding_data$Total_Estimate, SplitRatio = 0.8)
training_data=subset(wedding_data,split == TRUE)
testing_data=subset(wedding_data,split == FALSE)

dim(training_data)
dim(testing_data)

#Feature scaling
training_data[,5:6]=scale(training_data[,5:6])
testing_data[,5:6]=scale(testing_data[,5:6])

#Regression with Multiple Linear regression model
regressor=lm(formula= Total_Estimate ~ .,
             data = training_data)

y_pred=predict(regressor,newdata = testing_data)


summary(regressor)
summary(regressor)$r.squared
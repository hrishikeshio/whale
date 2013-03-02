# makes the random forest submission

library(randomForest)
library(ROCR)
train <- read.table("reduced_train.csv", sep=" ", header=FALSE)
test  <- read.table("reduced_test.csv",  sep=" ", header=FALSE)
n     <- nrow( train )
clip_labels <- read.csv("../Raw/data/train.csv")
labels <- factor( clip_labels$label )
train_labels  <- labels[1:n]

rf <- randomForest( train, train_labels, xtest=test, ntree=300, do.trace=TRUE )

predictions <- as.integer( levels(train_labels)[rf$test$predicted] )

write(predictions, file="rf_benchmark.csv", ncolumns=1) 

#pred = prediction(predictions, true_labels);
#auc.tmp = performance(pred,"auc");
#auc = as.numeric(auc.tmp@y.values);


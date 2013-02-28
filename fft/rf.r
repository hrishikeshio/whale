# makes the random forest submission

library(randomForest)
library(ROCR)
full_set  <- read.table("total.csv", sep=" ", header=FALSE)
n <- nrow( full_set )

clip_labels <- read.csv("../Raw/data/train.csv")
m <- 1000

train <- full_set[1:m,]
test  <- full_set[(m+1):n,]
labels <- factor( clip_labels$label )

train_labels  <- labels[1:m]
true_labels   <- labels[(m+1):n]

rf <- randomForest(train, train_labels, xtest=test, ntree=100,do.trace=TRUE)

predictions <- as.integer( levels(train_labels)[rf$test$predicted] )

write(predictions, file="rf_benchmark.csv", ncolumns=1) 

pred = prediction(predictions, true_labels);
auc.tmp = performance(pred,"auc");
auc = as.numeric(auc.tmp@y.values);


clc 
clear all 
close all
load blind_squeezenet.mat
imdsTest = imageDatastore("C:\Users\mnsle\Downloads\aptos2019-blindness- detection\test","IncludeSubfolders",true,"LabelSource","foldernames"); 
augimdsTest = augmentedImageDatastore([256 256 3],imdsTest);
YPred = classify(trainedNetwork_1,augimdsTest); 
Yactual = imdsTest.Labels; confusionchart(Yactual,YPred,...
    'RowSummary','row-normalized', ...
  'ColumnSummary','column-normalized')
C=confusionmat(Yactual,YPred) 
[row,col]= size(C); 
n_class=row;
for i=1:n_class
  TP(i)=C(i,i); FN(i)=sum(C(i,:))-C(i,i);
  FP(i)=sum(C(:,i))-C(i,i);
  TN(i)=sum(C(:))-TP(i)-FP(i)-FN(i);
  Accuracy(i) =(TP(i)+TN(i))/(TP(i)+TN(i)+FP(i)+FN(i));
  Error(i)=1-Accuracy(i); Recall(i)=TP(i)/(TP(i)+FN(i));
  Precision(i)=TP(i)/(TP(i)+FP(i));
  Specificity(i) = TN(i)/(TN(i)+FP(i));
  Sensitivity(i) = TP(i)/(TP(i)+FN(i)); FPR(i)=1-Specificity(i);
  beta=1;
  F1_score(i)=( (1+(beta^2))*(Recall(i).*Precision(i))) ./ ( (beta^2)*(Precision(i)+Recall(i)));
end
 Accuracy1=mean(Accuracy); 
 Error1=mean(Error); Recall1=mean(Recall); 
 Precision1=mean(Precision); Specificity1=mean(Specificity); 
 Sensitivity1=mean(Sensitivity); 
 FPR1=mean(FPR);
 F1_score1=mean(F1_score);

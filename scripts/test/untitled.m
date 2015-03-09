clear all;
cd flat/stats
fileID=fopen('strdrop','r');
strdrop = fread(fileID,'single');

n=length(strdrop)
disp('Average stress drop is 'num2str(strdrop(n)/1e6));

fileID=fopen('estrain','r');
estrain = fread(fileID,'single');
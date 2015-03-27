clear all;
nx=35;
ny=35;
nz=22;
dx=100;

x=(-(nx-1)/2:(nx-1)/2)*dx;
y=(-(nx-1)/2:(nx-1)/2)*dx;
[ya,xa]=meshgrid(x,y);
cd flat-g/out

fid=fopen('tsoriginal','r');
ts0=fread(fid,'single');
ts0=reshape(ts0,nx,ny);
figure(1)
pcolor(xa,ya,ts0);
colorbar
sqrt(sum(ts0(:))/70e6*1e4/pi)

figure(2)
fid=fopen('tsfinal','r');
tsf=fread(fid,'single');
tsf=reshape(tsf,nx,ny);
pcolor(xa,ya,tsf);
colorbar
figure(3)
pcolor(xa,ya,tsf-ts0);
colorbar

figure(4)
fid=fopen('slip_x','r');
ts0=fread(fid,'single');
ts0=reshape(ts0,nx,ny);
pcolor(xa,ya,ts0);
colorbar

figure(5)
fid=fopen('trup','r');
ts0=fread(fid,'single');
ts0=reshape(ts0,nx,ny);
pcolor(xa,ya,ts0);
colorbar
su=0;
for i=1:nx
    for j=1:ny
        if ts0(i,j)<1e8 
            su=su+1;
        end
    end
end
su
sqrt(su*1e4/pi)


function wrap_project


python_package_name = 'example_project'; 
matlab_project_url  = 'https://github.com/MPython-Package-Factory/example-project-matlab.git'; 
[~, matlab_project_name] = fileparts(matlab_project_url); 
mpython_url = 'https://github.com/MPython-Package-Factory/mpython.git';

[filedir, ~, ~] = fileparts(mfilename('fullpath'));
python_package_path = fullfile(filedir, '..'); 

oldpath = path; 
restoredefaultpath; 

cpath = pwd; 

cd(filedir);

mkdir('external');
cd('external');

if ~exist(matlab_project_name, 'dir')
    system(sprintf('git clone --depth=1 %s', matlab_project_url)); 
else 
    system(sprintf('git -C %s pull', matlab_project_name));
end

if ~exist('mpython', 'dir')
    system(sprintf('git clone --depth=1 %s', mpython_url));
else 
    system('git -C mpython pull');
end

cd('..'); 

addpath(fullfile(filedir, 'external', 'mpython'));
addpath(fullfile(filedir, 'external', matlab_project_name));

mkdir('build'); 
srcpath   = fullfile('external', matlab_project_name);
buildpath = fullfile('build', matlab_project_name); 
copyfile(srcpath, buildpath); 

ignored = {
    '.git'
    '.github'
};
for d = ignored
    try 
        rmdir(fullfile(buildpath, d{1}), 's'); 
    end
    try 
        delete(fullfile(buildpath, d{1}));
    end
end


mpython_compile(buildpath, python_package_path, python_package_name)


mpython_wrap( ...
    buildpath, ...
    python_package_path, ...
    python_package_name, ...
    true, ...
    fullfile(filedir, 'templates'))

addpath(oldpath);
cd(cpath); 
end

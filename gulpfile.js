let gulp = require('gulp');
let exec = require('child_process').exec;


gulp.task('tailwindcss', function (cb) {
    exec(
    'npx tailwindcss -i ./useFilesFromYandexDisk/useFilesFromYandexDisk/static/useFilesFromYandexDisk/css/input.css'+
    ' -o ./useFilesFromYandexDisk/useFilesFromYandexDisk/static/useFilesFromYandexDisk/css/output.css --watch',
    function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
    cb(err);
    });
});


gulp.task('watch', function(){
  gulp.watch('./useFilesFromYandexDisk/**/**.html', gulp.series(['tailwindcss']));
//  gulp.watch('./baseProject/baseProject/static/baseProject/css/input.css',
//  gulp.series(['tailwindcss']));
});

exports.default = gulp.series(['tailwindcss', 'watch']);
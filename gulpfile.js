var gulp = require('gulp'),
    p = require('gulp-load-plugins')();

gulp.task('styles', function () {
    gulp.src('./youmu/static/sass/base.scss')
    .pipe(p.sass({
        // outputStyle: 'compressed'    // Uncomment to use compressed style in production
    }))
    .pipe(p.autoprefixer({
        browsers: ['last 3 versions'],
        cascade: false
    }))
    .pipe(gulp.dest('./youmu/static/css/'))
    .pipe(p.livereload());
});

gulp.task('watch', function() {
    p.livereload.listen();

    gulp.watch('./youmu/static/sass/**/*.scss', ['styles']);
});

gulp.task('default', function() {
    gulp.start('watch');
});

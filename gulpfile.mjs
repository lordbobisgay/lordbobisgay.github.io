import gulp from 'gulp';
import webp from 'gulp-webp';

function convertImages() {
    return gulp.src('assets/img/portfolio/**/*.png')
      .pipe(webp())
      .pipe(gulp.dest('assets/img/webp'));
}

function watchImages() {
    gulp.watch('assets/img/portfolio/**/*.png', convertImages);
}

export default watchImages;
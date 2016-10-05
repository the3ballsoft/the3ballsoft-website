var gulp = require('gulp');
var gutil = require('gulp-util');
var concat = require('gulp-concat');
var sass = require('gulp-sass');
var minifyCss = require('gulp-minify-css');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');
var connect = require('gulp-connect');

var paths = {
  sass: ['./src/sass/**/**/*'],
  js: ['./src/js/**/**/*.js'],
  vendor: ['./src/libs/**/*.js'],
};

gulp.task('default', ['sass', 'js', 'vendor']);

/*
  | --- SASS -----------------------------------------------
  */

gulp.task('sass', function(done) {
  gulp.src('./src/sass/main.scss')
  .pipe(sass())
  .pipe(minifyCss({
    keepSpecialComments: 0
  }))
  .pipe(rename({ extname: '.min.css' }))
  .pipe(gulp.dest('./static/css'))
  .pipe(connect.reload())
  .on('end', done);
});

/*
  | --- JS -------------------------------------------------
  */
gulp.task('vendor', function(done) {
  var vendorFiles = require('./vendor.json');
  gulp.src(vendorFiles)
  .pipe(concat('vendor.js'))
  .pipe(uglify())
  .pipe(rename({ extname: '.min.js' }))
  .pipe(gulp.dest('./static/js/'))
  .pipe(connect.reload())
  .on('end', done);
});

gulp.task('js', function(done) {
  gulp.src(['./src/js/**/**/*.js', ])
  .pipe(concat('bundle.js'))
  .pipe(uglify())
  .pipe(rename({ extname: '.min.js' }))
  .pipe(gulp.dest('./static/js/'))
  .pipe(connect.reload())
  .on('end', done);
});

gulp.task('watch', function() {
  gulp.watch(paths.sass, ['sass']);
  gulp.watch(paths.js, ['js']);
  gulp.watch(paths.vendor, ['vendor']);
});


gulp.task('serve', function() {
  gulp.watch(paths.sass, ['sass']);
  gulp.watch(paths.js, ['js']);
  gulp.watch(paths.vendor, ['vendor']);

  connect.server({
    root: 'public',
    port: 3000,
    host: 'localhost',
    livereload: true,
    fallback: 'index.html'
  });
});


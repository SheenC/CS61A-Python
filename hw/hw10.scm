(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
   (if (= n 0)
        start
        (combiner (accumulate combiner
                              start
                              (- n 1)
                              term)
                  (term n))))

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
   (if (= n 0)
        start
        (accumulate-tail combiner (combiner (term n) start) (- n 1) term)
    )
)


(define (partial-sums stream)
  'YOUR-CODE-HERE
   (define (helper n stream)
           (if (null? stream)
                nil
                (cons-stream (+ n (car stream)) (helper (+ n (car stream)) (cdr-stream stream)))
           )
   )
  (helper 0 stream)
)


(define (rle s)
  'YOUR-CODE-HERE
  (define (helper node prev count)
     (cond ((null? node) (cons-stream (list prev count) nil))
           ((= prev (car node)) (helper (cdr-stream node) prev (+ count 1)))
           (else (cons-stream (list prev count) (helper (cdr-stream node) (car node) 1)))))
     (if (null? s)
         ()
         (helper (cdr-stream s) (car s) 1)))

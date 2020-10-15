(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s)))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cdr (cdr s))))
)

(define (sign x)
  'YOUR-CODE-HERE
  (cond
       ((< x 0) -1)
       ((= x 0) 0)
       ((> x 0) 1)
  )
)

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
  (cond
       ((= n 0) 1)
       ((even? n) (pow (square b) (/ n 2)))
       (else (* b (pow (square b) (/ (- n 1) 2))))
  )
)

(define (ordered? s)
  'YOUR-CODE-HERE
  (if (or (null? s) (null? (cdr s)))
      True
      (and (<= (car s) (cadr s)) (ordered? (cdr s)))
  )
)

(define (empty? s) (null? s))

(define (add s v)
    'YOUR-CODE-HERE
    (cond
         ((empty? s) (list v))
         ((> (car s) v) (cons v s))
         ((< (car s) v) (cons (car s) (add (cdr s) v)))
         ((= (car s) v) s)
    )
)

; Sets as sorted lists
(define (contains? s v)
    'YOUR-CODE-HERE
    (cond
         ((empty? s) False)
         ((= (car s) v) True)
         (else (contains? (cdr s) v))
    )
    )

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (intersect s t)
    'YOUR-CODE-HERE
    (cond
         ((or (empty? s) (empty? t)) nil)
         ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
         ((< (car s) (car t)) (intersect (cdr s) t))
         ((> (car s) (car t)) (intersect s (cdr t)))
    )
    )

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    'YOUR-CODE-HERE
    (cond
         ((empty? s) t)
         ((empty? t) s)
         ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
         ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
         (else (cons (car t) (union s (cdr t))))
    )
)

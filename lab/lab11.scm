


(define-macro (def func bindings body)
    'YOUR-CODE-HERE
    (list 'define func (list 'lambda bindings body))
)

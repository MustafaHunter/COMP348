(defun f (lst)
  (cond ((null lst) '())
        ((null (rest lst)) lst)
        ((equal (first lst) (second lst)) (f (rest lst)))
        (t (cons (first lst) (f (rest lst))))))
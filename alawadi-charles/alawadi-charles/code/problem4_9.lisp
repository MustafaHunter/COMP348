(defun is-memberp (element set)
  (member element set))

(defun equal-setsp (set1 set2)
  (and (subsetp set1 set2) (subsetp set2 set1)))

(defvar set1 '(1 2 3 4 5))
(defvar set2 '(3 4 5 6 7))
(defvar set3 '(1 2 3 4 5))
(defvar set4 '(3 4 5 2 1))

; Test is-memberp
(print (is-memberp 3 set1)) ; Returns T
(print (is-memberp 6 set1)) ; Returns NIL

; Test equal-setsp
(print (equal-setsp set1 set2)) ; Returns NIL
(print (equal-setsp set1 set3)) ; Returns T
(print (equal-setsp set2 set4)) ; Returns NIL

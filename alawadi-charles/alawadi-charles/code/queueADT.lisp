

(setf stack1 '())
(setf stack2 '())

(defun length (lst)
(if (null lst)
0
(+ 1 (length (cdr lst)))))

(defun reverse (lst)
    (cond ((null lst) '())
        (t (append (reverse (cdr lst)) (list (car lst))))))

(defun enqueue ( queue element )
(let ((count1 length(stack1)) (count2 length(stack2))
) (if (zerop count2)
    (append '(element) queue)
    (append '(element) queue)
    )

;;  (if (and (not (zerop count1))       --->For dequeue
;;        (zerop count2))
;;    1
;;    0)  

)
)
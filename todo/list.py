

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
		public = request.form['public']
		item1 = request.form['item1']
		items = [item1]
        error = None

        if not title:
            error = 'Title is required.'
        if error is not None:
            flash(error)

        else:
            db = sqlite3.connect('lists.db')
            db.execute('''CREATE TABLE IF NOT EXISTS listname (
				id integer PRIMARY KEY AUTOINCREMENT,
				task text,
				author text,
				public integer);'''.replace('listname', title))

			for item in items:
				db.execute(
					'INSERT INTO listname (task, author, public) VALUES (?, ?, ?)'.replace(
						'listname', title), (item, g.user['id'], public))

            db.commit()
            return redirect(url_for('list.index'))

    return render_template('list/create.html')


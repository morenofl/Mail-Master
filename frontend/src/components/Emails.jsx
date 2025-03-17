import { useState, useEffect } from 'react';
import { testConnection, getTopEmails } from '../api.js';

export default function Emails() {
	const [emails, setEmails] = useState([]);

	const fetchData = async () => {
		try {
			const data = await getTopEmails();
			console.log(data);
			setEmails(data);
		} catch (error) {
			console.error('Error fetching emails:', error);
		}
	}

	useEffect(() => {
		testConnection();
	}, []);
	useEffect(() => {
		fetchData();
	}, []);
	return (
		<>
			<div>
				<h1>Top Email Senders</h1>
				<ul>
					{emails.map((email, index) => {
						return (
							<li key={index}>
								{email.email} - {email.count} emails
							</li>
						)

					})}
				</ul>
			</div>
		</>
	)
}

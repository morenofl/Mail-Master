import { useState, useEffect } from 'react';
import { testConnection, getTopEmails, fetchEmails } from '../api.js';
import './Emails.css';

export default function Emails() {
	const [emails, setEmails] = useState([]);

	const fetchData = async () => {
		try {
			const data = await fetchEmails();
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
			<div className="pageContainer">
				<h1>Top Email Senders</h1>
				<ul>
					{emails.map((email, index) => {
						return (
							<li key={index}>
								{email.address} - {email.count} emails
							</li>
						)

					})}
				</ul>
			</div>
		</>
	)
}

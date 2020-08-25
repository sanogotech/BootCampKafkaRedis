package com.mitrais.persistence.service;

import org.springframework.dao.DataIntegrityViolationException;
import com.mitrais.persistence.entity.MUser;

public interface CommonDAO {

	public Object save(Object o) throws DataIntegrityViolationException;
	
	public Object saveMUser(MUser o) throws DataIntegrityViolationException;
	
	public Object update(Object o);
	
	@SuppressWarnings("rawtypes")
	public Object get(String id, Class cls);
	
	@SuppressWarnings("rawtypes")
	public Object get(Long id, Class cls);
	
	@SuppressWarnings("rawtypes")
	public void delete(String id, Class cls);
	
	@SuppressWarnings("rawtypes")
	public void delete(Long id, Class cls);
	
}
